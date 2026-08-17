# BTCP skills

Portable Agent Skills, curated collections, and optional end-to-end agents from Beacon-Taylor Computational Partners.

## Repository layout

- `skills/` is the canonical source for standalone, cross-agent skills.
- `catalog/skills.json` contains gallery metadata that does not belong in `SKILL.md`.
- `catalog/plugins.json` defines independently installable collections and agent packages.
- `catalog/agents.json` describes optional end-to-end agents built from canonical skills.
- `plugins/<plugin-name>/` contains generated skill bundles plus OpenAI and Claude manifests.
- `packages/skills/` and `packages/plugins/` receive generated ZIP archives.

Plugin folders stay flat because the OpenAI marketplace resolves them as `./plugins/<plugin-name>`. The catalog records whether each package is a collection or an agent.

## Add a skill

Create `skills/<skill-name>/SKILL.md` using lowercase kebab-case for the directory and frontmatter name. Keep the portable frontmatter limited to `name` and `description`, then add its gallery record to `catalog/skills.json`.

To bundle skills for hosted products, add their names to a package in `catalog/plugins.json`. Do not edit generated copies under `plugins/*/skills/` directly.

Run `npm test` before publishing. Run `npm run package` to generate ZIP archives for every skill and plugin.

## Install locally

Once this repository is public, install an individual skill with:

```sh
npx skills add JoshMayerr/btcp-skills --skill <skill-name>
```

Provider-specific plugin installation instructions will be published with the first released skill.
