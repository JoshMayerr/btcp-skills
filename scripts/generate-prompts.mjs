import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const catalog = JSON.parse(await readFile(path.join(repoRoot, "catalog", "skills.json"), "utf8"));
const distribution = JSON.parse(await readFile(path.join(repoRoot, "catalog", "distribution.json"), "utf8"));
const createRoot = path.join(repoRoot, "prompts", "create");
const oneOffRoot = path.join(repoRoot, "prompts", "one-off");
const reducedRoot = path.join(repoRoot, "prompts", "reduced");

const expand = (template, skill) =>
  template.replaceAll("{name}", skill.name).replaceAll("{version}", skill.version);
const skillBody = (source) => source.replace(/^---\n[\s\S]*?\n---\n?/, "").trim();

await Promise.all([
  rm(createRoot, { recursive: true, force: true }),
  rm(oneOffRoot, { recursive: true, force: true }),
]);
await Promise.all([
  mkdir(createRoot, { recursive: true }),
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
    await writeFile(
      path.join(createRoot, `${skill.name}.md`),
      `Use $skill-creator to create a skill named “${skill.name}”.

${canonicalSource}

Preserve its intended triggers, workflow, safeguards, and output requirements. Include every referenced script, asset, and reference file supplied by the canonical package. Create it in the default personal skills directory for this environment, validate the completed skill, then tell me where it was installed and how to invoke it.

Do not substantially rewrite or omit behavior from the canonical source.
`,
    );
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

if (builderCount === 0) await writeFile(path.join(createRoot, ".gitkeep"), "");
if (oneOffCount === 0) await writeFile(path.join(oneOffRoot, ".gitkeep"), "");

console.log(
  `Generated ${builderCount} builder prompt${builderCount === 1 ? "" : "s"} and ${oneOffCount} one-off prompt${oneOffCount === 1 ? "" : "s"}.`,
);
