import { mkdir, readFile, readdir, rm } from "node:fs/promises";
import { execFile } from "node:child_process";
import path from "node:path";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";

const run = promisify(execFile);
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const skillRoot = path.join(repoRoot, "skills");
const pluginRoot = path.join(repoRoot, "plugins");
const packageRoot = path.join(repoRoot, "packages");
const pluginCatalog = JSON.parse(
  await readFile(path.join(repoRoot, "catalog", "plugins.json"), "utf8"),
);

const entries = await readdir(skillRoot, { withFileTypes: true });
const skillNames = entries
  .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
  .map((entry) => entry.name)
  .sort();

const skillPackageRoot = path.join(packageRoot, "skills");
const pluginPackageRoot = path.join(packageRoot, "plugins");
await mkdir(skillPackageRoot, { recursive: true });
await mkdir(pluginPackageRoot, { recursive: true });

for (const skillName of skillNames) {
  const archivePath = path.join(skillPackageRoot, `${skillName}.zip`);
  await rm(archivePath, { force: true });
  await run("zip", ["-qr", archivePath, skillName], { cwd: skillRoot });
}

for (const plugin of pluginCatalog.plugins) {
  const archivePath = path.join(pluginPackageRoot, `${plugin.name}.zip`);
  await rm(archivePath, { force: true });
  await run("zip", ["-qr", archivePath, plugin.name], { cwd: pluginRoot });
}

console.log(
  `Packaged ${skillNames.length} skill${skillNames.length === 1 ? "" : "s"} and ${pluginCatalog.plugins.length} plugin${pluginCatalog.plugins.length === 1 ? "" : "s"}.`,
);
