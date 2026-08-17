import { cp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourceRoot = path.join(repoRoot, "skills");
const pluginCatalog = JSON.parse(
  await readFile(path.join(repoRoot, "catalog", "plugins.json"), "utf8"),
);

let synced = 0;

for (const plugin of pluginCatalog.plugins) {
  const pluginRoot = path.resolve(repoRoot, plugin.sourcePath);
  const destinationRoot = path.join(pluginRoot, "skills");

  if (!pluginRoot.startsWith(`${path.join(repoRoot, "plugins")}${path.sep}`)) {
    throw new Error(`Plugin source escapes plugins/: ${plugin.sourcePath}`);
  }

  await rm(destinationRoot, { recursive: true, force: true });
  await mkdir(destinationRoot, { recursive: true });

  for (const skillName of [...plugin.skills].sort()) {
    await cp(path.join(sourceRoot, skillName), path.join(destinationRoot, skillName), {
      recursive: true,
    });
    synced += 1;
  }

  if (plugin.skills.length === 0) {
    await writeFile(path.join(destinationRoot, ".gitkeep"), "");
  }
}

console.log(
  `Synced ${synced} skill bundle entr${synced === 1 ? "y" : "ies"} across ${pluginCatalog.plugins.length} plugin${pluginCatalog.plugins.length === 1 ? "" : "s"}.`,
);
