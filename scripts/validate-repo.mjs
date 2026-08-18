import { access, readFile, readdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const skillRoot = path.join(repoRoot, "skills");
const draftRoot = path.join(repoRoot, "drafts");
const pluginRoot = path.join(repoRoot, "plugins");
const namePattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const versionPattern = /^\d+\.\d+\.\d+$/;

const readJson = async (relativePath) =>
  JSON.parse(await readFile(path.join(repoRoot, relativePath), "utf8"));

const assertCatalog = (catalog, key, relativePath) => {
  if (catalog.schemaVersion !== 1 || !Array.isArray(catalog[key])) {
    throw new Error(`${relativePath} must use schemaVersion 1 and contain a ${key} array.`);
  }
};

const assertUnique = (values, label) => {
  if (new Set(values).size !== values.length) {
    throw new Error(`${label} must not contain duplicates.`);
  }
};

const listFiles = async (directory, prefix = "") => {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (entry.name === ".gitkeep") continue;
    const relativePath = path.join(prefix, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listFiles(path.join(directory, entry.name), relativePath)));
    } else if (entry.isFile()) {
      files.push(relativePath);
    } else {
      throw new Error(`Unsupported filesystem entry: ${path.join(directory, entry.name)}`);
    }
  }
  return files.sort();
};

const assertDirectoriesEqual = async (canonicalDirectory, bundledDirectory, label) => {
  const canonicalFiles = await listFiles(canonicalDirectory);
  const bundledFiles = await listFiles(bundledDirectory);

  if (JSON.stringify(canonicalFiles) !== JSON.stringify(bundledFiles)) {
    throw new Error(`${label} has missing or extra files. Run npm run sync:plugins.`);
  }

  for (const relativePath of canonicalFiles) {
    const [canonical, bundled] = await Promise.all([
      readFile(path.join(canonicalDirectory, relativePath)),
      readFile(path.join(bundledDirectory, relativePath)),
    ]);
    if (!canonical.equals(bundled)) {
      throw new Error(`${label}/${relativePath} differs from its canonical source.`);
    }
  }
};

const skillsCatalog = await readJson("catalog/skills.json");
const pluginsCatalog = await readJson("catalog/plugins.json");
const agentsCatalog = await readJson("catalog/agents.json");
const distribution = await readJson("catalog/distribution.json");
const codexMarketplace = await readJson(".agents/plugins/marketplace.json");
const claudeMarketplace = await readJson(".claude-plugin/marketplace.json");

assertCatalog(skillsCatalog, "skills", "catalog/skills.json");
assertCatalog(pluginsCatalog, "plugins", "catalog/plugins.json");
assertCatalog(agentsCatalog, "agents", "catalog/agents.json");

if (
  distribution.schemaVersion !== 1 ||
  !distribution.repositoryUrl ||
  !distribution.skillSourceUrlTemplate?.includes("{name}") ||
  !distribution.skillArchiveUrlTemplate?.includes("{name}") ||
  !distribution.skillArchiveUrlTemplate?.includes("{version}")
) {
  throw new Error("catalog/distribution.json must define the repository, skill source, and versioned archive URL templates.");
}

const skillEntries = await readdir(skillRoot, { withFileTypes: true });
const skillNames = skillEntries
  .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
  .map((entry) => entry.name)
  .sort();

const draftEntries = await readdir(draftRoot, { withFileTypes: true });
const draftNames = draftEntries
  .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
  .map((entry) => entry.name)
  .sort();

for (const [skillName, root] of [
  ...skillNames.map((name) => [name, skillRoot]),
  ...draftNames.map((name) => [name, draftRoot]),
]) {
  if (!namePattern.test(skillName) || skillName.length > 64) {
    throw new Error(`Invalid skill directory name: ${skillName}`);
  }

  const skillPath = path.join(root, skillName, "SKILL.md");
  await access(skillPath);
  const source = await readFile(skillPath, "utf8");
  const frontmatter = source.match(/^---\n([\s\S]*?)\n---/);

  if (!frontmatter) {
    throw new Error(`${skillName}/SKILL.md is missing YAML frontmatter.`);
  }
  if (!frontmatter[1].includes(`name: ${skillName}`) || !frontmatter[1].includes("description:")) {
    throw new Error(`${skillName}/SKILL.md must include a matching name and a description.`);
  }
}

const catalogSkillNames = skillsCatalog.skills.map((skill) => skill.name);
assertUnique(catalogSkillNames, "Skill catalog names");
if (JSON.stringify([...catalogSkillNames].sort()) !== JSON.stringify([...skillNames, ...draftNames].sort())) {
  throw new Error("Catalog entries must match the published and draft skill directories exactly.");
}

for (const skill of skillsCatalog.skills) {
  if (!versionPattern.test(skill.version)) {
    throw new Error(`Invalid skill version: ${skill.name}@${skill.version}`);
  }
  if (!["draft", "published"].includes(skill.status)) {
    throw new Error(`Invalid status for ${skill.name}: ${skill.status}`);
  }
  if (!["self-contained", "source-linked", "unavailable"].includes(skill.builderMode)) {
    throw new Error(`Invalid builderMode for ${skill.name}: ${skill.builderMode}`);
  }
  if (!["standalone", "reduced", "unavailable"].includes(skill.promptMode)) {
    throw new Error(`Invalid promptMode for ${skill.name}: ${skill.promptMode}`);
  }

  const isPublished = skill.status === "published";
  if (isPublished !== skillNames.includes(skill.name)) {
    throw new Error(`${skill.name} must live in ${isPublished ? "skills" : "drafts"}/ for its status.`);
  }
  if (!isPublished && (skill.builderMode !== "unavailable" || skill.promptMode !== "unavailable")) {
    throw new Error(`Draft skill ${skill.name} cannot expose generated distribution prompts.`);
  }
  if (isPublished && skill.builderMode === "self-contained") {
    const entries = await readdir(path.join(skillRoot, skill.name), { withFileTypes: true });
    const bundledResources = entries.filter(
      (entry) => entry.name !== "SKILL.md" && entry.name !== "agents" && entry.name !== ".gitkeep",
    );
    if (bundledResources.length > 0) {
      throw new Error(`${skill.name} has bundled resources and must use source-linked builderMode.`);
    }
  }
  if (isPublished && skill.promptMode === "reduced") {
    await access(path.join(repoRoot, "prompts", "reduced", `${skill.name}.md`));
  }
}

const pluginNames = pluginsCatalog.plugins.map((plugin) => plugin.name);
assertUnique(pluginNames, "Plugin catalog names");
const pluginByName = new Map(pluginsCatalog.plugins.map((plugin) => [plugin.name, plugin]));

for (const plugin of pluginsCatalog.plugins) {
  if (!namePattern.test(plugin.name) || plugin.name.length > 64) {
    throw new Error(`Invalid plugin name: ${plugin.name}`);
  }
  if (!versionPattern.test(plugin.version)) {
    throw new Error(`Invalid plugin version: ${plugin.name}@${plugin.version}`);
  }
  if (!["collection", "agent"].includes(plugin.kind)) {
    throw new Error(`Invalid plugin kind for ${plugin.name}: ${plugin.kind}`);
  }
  if (plugin.sourcePath !== `plugins/${plugin.name}`) {
    throw new Error(`${plugin.name} must use sourcePath plugins/${plugin.name}.`);
  }
  assertUnique(plugin.skills, `Skills in plugin ${plugin.name}`);

  const sourceDirectory = path.resolve(repoRoot, plugin.sourcePath);
  if (!sourceDirectory.startsWith(`${pluginRoot}${path.sep}`)) {
    throw new Error(`Plugin source escapes plugins/: ${plugin.sourcePath}`);
  }
  await access(sourceDirectory);

  const [codexManifest, claudeManifest] = await Promise.all([
    readJson(`${plugin.sourcePath}/.codex-plugin/plugin.json`),
    readJson(`${plugin.sourcePath}/.claude-plugin/plugin.json`),
  ]);
  for (const [format, manifest] of [["OpenAI", codexManifest], ["Claude", claudeManifest]]) {
    if (manifest.name !== plugin.name || manifest.version !== plugin.version) {
      throw new Error(`${format} manifest for ${plugin.name} must match its catalog name and version.`);
    }
  }

  const mcpPath = path.join(sourceDirectory, ".mcp.json");
  try {
    await access(mcpPath);
    const mcpManifest = JSON.parse(await readFile(mcpPath, "utf8"));
    const servers = mcpManifest.mcpServers;
    if (!servers || typeof servers !== "object" || Array.isArray(servers)) {
      throw new Error(`${plugin.name}/.mcp.json must contain an mcpServers object.`);
    }
    for (const [serverName, server] of Object.entries(servers)) {
      if (!namePattern.test(serverName) || server?.type !== "http") {
        throw new Error(`${plugin.name}/.mcp.json has an invalid HTTP server: ${serverName}.`);
      }
      const url = new URL(server.url);
      if (url.protocol !== "https:") {
        throw new Error(`${plugin.name}/.mcp.json must use HTTPS for ${serverName}.`);
      }
    }
  } catch (error) {
    if (error?.code !== "ENOENT") throw error;
  }

  for (const skillName of plugin.skills) {
    if (!skillNames.includes(skillName)) {
      throw new Error(`${plugin.name} references unknown skill ${skillName}.`);
    }
    await assertDirectoriesEqual(
      path.join(skillRoot, skillName),
      path.join(sourceDirectory, "skills", skillName),
      `${plugin.name}/skills/${skillName}`,
    );
  }

  const bundledEntries = (await readdir(path.join(sourceDirectory, "skills"), { withFileTypes: true }))
    .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
    .map((entry) => entry.name)
    .sort();
  if (JSON.stringify(bundledEntries) !== JSON.stringify([...plugin.skills].sort())) {
    throw new Error(`${plugin.name}/skills does not match catalog/plugins.json. Run npm run sync:plugins.`);
  }
}

if (!Array.isArray(codexMarketplace.plugins) || !Array.isArray(claudeMarketplace.plugins)) {
  throw new Error("Both marketplace manifests must contain a plugins array.");
}

const codexNames = codexMarketplace.plugins.map((plugin) => plugin.name);
const claudeNames = claudeMarketplace.plugins.map((plugin) => plugin.name);
assertUnique(codexNames, "OpenAI marketplace plugin names");
assertUnique(claudeNames, "Claude marketplace plugin names");
for (const marketplaceNames of [codexNames, claudeNames]) {
  if (JSON.stringify([...marketplaceNames].sort()) !== JSON.stringify([...pluginNames].sort())) {
    throw new Error("Marketplace plugin entries must match catalog/plugins.json exactly.");
  }
}

for (const entry of codexMarketplace.plugins) {
  const plugin = pluginByName.get(entry.name);
  if (entry.source?.source !== "local" || entry.source?.path !== `./${plugin.sourcePath}`) {
    throw new Error(`OpenAI marketplace source is incorrect for ${entry.name}.`);
  }
}
for (const entry of claudeMarketplace.plugins) {
  const plugin = pluginByName.get(entry.name);
  if (entry.source !== `./${plugin.sourcePath}` || entry.version !== plugin.version) {
    throw new Error(`Claude marketplace source or version is incorrect for ${entry.name}.`);
  }
}

const agentNames = agentsCatalog.agents.map((agent) => agent.name);
assertUnique(agentNames, "Agent catalog names");
for (const agent of agentsCatalog.agents) {
  if (!namePattern.test(agent.name) || agent.name.length > 64 || !versionPattern.test(agent.version)) {
    throw new Error(`Invalid agent catalog entry: ${agent.name}`);
  }
  const plugin = pluginByName.get(agent.plugin);
  if (!plugin || plugin.kind !== "agent") {
    throw new Error(`${agent.name} must reference a plugin whose kind is agent.`);
  }
  if (agent.version !== plugin.version) {
    throw new Error(`${agent.name} and plugin ${agent.plugin} must use the same version.`);
  }
}

const agentPluginNames = pluginsCatalog.plugins
  .filter((plugin) => plugin.kind === "agent")
  .map((plugin) => plugin.name)
  .sort();
const catalogAgentPluginNames = agentsCatalog.agents.map((agent) => agent.plugin).sort();
if (JSON.stringify(agentPluginNames) !== JSON.stringify(catalogAgentPluginNames)) {
  throw new Error("Every agent plugin must have exactly one catalog/agents.json entry.");
}

const promptNames = async (directory) =>
  (await readdir(path.join(repoRoot, "prompts", directory), { withFileTypes: true }))
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => entry.name.slice(0, -3))
    .sort();

const expectedBuilderPrompts = skillsCatalog.skills
  .filter((skill) => skill.status === "published" && skill.builderMode !== "unavailable")
  .map((skill) => skill.name)
  .sort();
const expectedOneOffPrompts = skillsCatalog.skills
  .filter((skill) => skill.status === "published" && skill.promptMode !== "unavailable")
  .map((skill) => skill.name)
  .sort();
const [builderPrompts, oneOffPrompts] = await Promise.all([
  promptNames("create"),
  promptNames("one-off"),
]);
if (JSON.stringify(builderPrompts) !== JSON.stringify(expectedBuilderPrompts)) {
  throw new Error("Generated builder prompts do not match the published skill catalog.");
}
if (JSON.stringify(oneOffPrompts) !== JSON.stringify(expectedOneOffPrompts)) {
  throw new Error("Generated one-off prompts do not match the published skill catalog.");
}

console.log(
  `Validated ${skillNames.length} published skill${skillNames.length === 1 ? "" : "s"}, ${draftNames.length} draft${draftNames.length === 1 ? "" : "s"}, ${pluginNames.length} plugin${pluginNames.length === 1 ? "" : "s"}, and ${agentNames.length} agent${agentNames.length === 1 ? "" : "s"}.`,
);
