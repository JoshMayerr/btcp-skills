# Repository instructions

- Treat `skills/` as the canonical source. Do not edit generated copies under `plugins/*/skills/` directly.
- Define collection and agent packages in `catalog/plugins.json`; keep plugin folders flat as `plugins/<plugin-name>`.
- Define end-to-end agent metadata in `catalog/agents.json` only when a workflow needs its own prompt, tool policy, or orchestration.
- Keep skill directory names and `name` frontmatter in lowercase kebab-case and under 64 characters.
- Keep portable `SKILL.md` frontmatter limited to `name` and `description`. Put gallery metadata in `catalog/skills.json`.
- Keep each `SKILL.md` concise and move detailed material into `references/`, deterministic helpers into `scripts/`, and output resources into `assets/`.
- Run `npm test` after editing skills, catalogs, or plugin manifests. Run `npm run package` before publishing downloadable ZIP archives.
- Use sentence case for user-facing copy. Preserve conventional capitalization for BTCP and AI.
