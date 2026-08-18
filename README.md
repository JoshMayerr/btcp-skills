# BTCP skills

Portable Agent Skills, curated collections, and optional end-to-end agents from Beacon-Taylor Computational Partners.

## Repository layout

- `skills/` is the canonical source for standalone, cross-agent skills.
- `drafts/` holds incomplete skills that are not installable or visible in the gallery.
- `catalog/skills.json` contains gallery metadata that does not belong in `SKILL.md`.
- `catalog/plugins.json` defines independently installable collections and agent packages.
- `catalog/agents.json` describes optional end-to-end agents built from canonical skills.
- `catalog/distribution.json` defines versioned source and release URLs used by generated prompts.
- `plugins/<plugin-name>/` contains generated skill bundles plus OpenAI and Claude manifests.
- `prompts/create/` contains copy-paste prompts for creating skills in ChatGPT.
- `prompts/one-off/` contains copy-paste prompts for using supported workflows without installation.
- `packages/skills/` and `packages/plugins/` receive generated ZIP archives.

Plugin folders stay flat because the OpenAI marketplace resolves them as `./plugins/<plugin-name>`. The catalog records whether each package is a collection or an agent.

## Add a skill

Create `skills/<skill-name>/SKILL.md` using lowercase kebab-case for the directory and frontmatter name. Keep the portable frontmatter limited to `name` and `description`, then add its gallery record to `catalog/skills.json`.

Keep incomplete work under `drafts/` with `status` set to `draft`. Move it to `skills/` and set `status` to `published` when it is ready. For a published skill, set `builderMode` to `self-contained`, `source-linked`, or `unavailable`, and set `promptMode` to `standalone`, `reduced`, or `unavailable`. A reduced one-off prompt must be authored at `prompts/reduced/<skill-name>.md`; the other public prompt files are generated.

To bundle skills for hosted products, add their names to a package in `catalog/plugins.json`. Do not edit generated copies under `plugins/*/skills/` directly.

Run `npm test` before publishing. It regenerates plugin bundles and gallery prompts before validation. Run `npm run package` to generate ZIP archives for every published skill and plugin.

## Install locally

Once this repository is public, install an individual skill with:

```sh
npx skills add JoshMayerr/btcp-skills --skill <skill-name>
```

Provider-specific plugin installation instructions will be published with the first released skill.

## Gallery actions

Each published skill can expose up to four actions: install from the repository, copy a “Create in ChatGPT” prompt, download a release ZIP, and copy a one-off prompt. Generated builder prompts use immutable `<skill-name>-v<version>` release tags rather than the moving `main` branch.
