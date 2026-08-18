import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const catalog = JSON.parse(await readFile(path.join(repoRoot, "catalog", "skills.json"), "utf8"));
const distribution = JSON.parse(await readFile(path.join(repoRoot, "catalog", "distribution.json"), "utf8"));
const createRoot = path.join(repoRoot, "prompts", "create");
const createClaudeRoot = path.join(repoRoot, "prompts", "create-claude");
const oneOffRoot = path.join(repoRoot, "prompts", "one-off");
const reducedRoot = path.join(repoRoot, "prompts", "reduced");

const expand = (template, skill) =>
  template.replaceAll("{name}", skill.name).replaceAll("{version}", skill.version);
const skillBody = (source) => source.replace(/^---\n[\s\S]*?\n---\n?/, "").trim();

await Promise.all([
  rm(createRoot, { recursive: true, force: true }),
  rm(createClaudeRoot, { recursive: true, force: true }),
  rm(oneOffRoot, { recursive: true, force: true }),
]);
await Promise.all([
  mkdir(createRoot, { recursive: true }),
  mkdir(createClaudeRoot, { recursive: true }),
  mkdir(oneOffRoot, { recursive: true }),
  mkdir(reducedRoot, { recursive: true }),
]);

let builderCount = 0;
let oneOffCount = 0;

for (const skill of [...catalog.skills].sort((a, b) => a.name.localeCompare(b.name))) {
  if (skill.status !== "published") continue;

  const source = await readFile(path.join(repoRoot, "skills", skill.name, "SKILL.md"), "utf8");
  const sourceUrl = expand(distribution.skillSourceUrlTemplate, skill);
  const archiveUrl = expand(distribution.skillArchiveUrlTemplate, skill);

  if (skill.builderMode !== "unavailable") {
    const canonicalSource = skill.builderMode === "self-contained"
      ? `Use this exact canonical SKILL.md as the source:\n\n\`\`\`markdown\n${source.trim()}\n\`\`\``
      : `Download the complete canonical package from:\n${archiveUrl}\n\nThe canonical SKILL.md is also available at:\n${sourceUrl}`;
    const builderPrompt = (opening) => `${opening}

${canonicalSource}

Preserve every supplied instruction, trigger, safeguard, script, reference, and asset. Do not rewrite or omit behavior. Install the skill in the default personal skills directory for this environment and validate the completed installation.

After installing it, tell me:
- Where it was installed
- Whether validation passed
- How to invoke it
- Whether I need to start a new task for it to become available

Then ask whether I also want to install the complete BTCP plugin, which includes the rest of the BTCP finance skills and its useful optional connectors. The plugin is great for financial workflows to make automation more reliable.
`;
    await Promise.all([
      writeFile(
        path.join(createRoot, `${skill.name}.md`),
        builderPrompt(`Use [$skill-creator](/Users/joshmayer/.codex/skills/.system/skill-creator/SKILL.md) to install the “${skill.title}” skill in my personal skills directory.`),
      ),
      writeFile(
        path.join(createClaudeRoot, `${skill.name}.md`),
        builderPrompt(`Use /skill-creator to install the “${skill.title}” skill in my personal skills directory.`),
      ),
    ]);
    builderCount += 1;
  }

  if (skill.promptMode !== "unavailable") {
    const oneOffSource = skill.promptMode === "standalone"
      ? skillBody(source)
      : (await readFile(path.join(reducedRoot, `${skill.name}.md`), "utf8")).trim();
    await writeFile(
      path.join(oneOffRoot, `${skill.name}.md`),
      `Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

${oneOffSource}
`,
    );
    oneOffCount += 1;
  }
}

if (builderCount === 0) {
  await writeFile(path.join(createRoot, ".gitkeep"), "");
  await writeFile(path.join(createClaudeRoot, ".gitkeep"), "");
}
if (oneOffCount === 0) await writeFile(path.join(oneOffRoot, ".gitkeep"), "");

console.log(
  `Generated ${builderCount} builder prompt${builderCount === 1 ? "" : "s"} and ${oneOffCount} one-off prompt${oneOffCount === 1 ? "" : "s"}.`,
);
