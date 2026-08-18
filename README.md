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
- `packages/skills/` contains the versioned ZIP archives linked from the skill gallery.
- `packages/plugins/` receives generated plugin ZIP archives for release workflows.

Plugin folders stay flat because the OpenAI marketplace resolves them as `./plugins/<plugin-name>`. The catalog records whether each package is a collection or an agent.

## Add a skill

Create `skills/<skill-name>/SKILL.md` using lowercase kebab-case for the directory and frontmatter name. Keep the portable frontmatter limited to `name` and `description`, then add its gallery record to `catalog/skills.json`.

Keep incomplete work under `drafts/` with `status` set to `draft`. Move it to `skills/` and set `status` to `published` when it is ready. For a published skill, set `builderMode` to `self-contained`, `source-linked`, or `unavailable`, and set `promptMode` to `standalone`, `reduced`, or `unavailable`. A reduced one-off prompt must be authored at `prompts/reduced/<skill-name>.md`; the other public prompt files are generated.

To bundle skills for hosted products, add their names to a package in `catalog/plugins.json`. Do not edit generated copies under `plugins/*/skills/` directly.

Run `npm test` before publishing. It regenerates plugin bundles and gallery prompts before validation. Run `npm run package` to generate ZIP archives for every published skill and plugin.

## Use the skills

### ChatGPT Work

Copy a one-off prompt from the [BTCP skill gallery](https://beacontaylor.com/skills) into a new conversation and attach the requested source files. To install the complete collection instead, open ChatGPT Plugins, select the plus button, and paste this repository into Source:

```text
https://github.com/JoshMayerr/btcp-skills
```

Add the marketplace, choose BTCP, and install `btcp-skills`.

### Claude

Copy a one-off prompt from the [BTCP skill gallery](https://beacontaylor.com/skills) into a new conversation and attach the requested source files. To reuse one skill, download its ZIP from the gallery, then open [Claude Skills](https://claude.ai/customize/skills) and upload it. ZIP upload is the Claude-only installation path.

### Claude Cowork

Open Customize → Plugins, add this repository as a marketplace, and install `btcp-skills`:

```text
https://github.com/JoshMayerr/btcp-skills
```

### Claude Code

Add the marketplace and install the collection:

```sh
claude plugin marketplace add JoshMayerr/btcp-skills
claude plugin install btcp-skills@btcp-skills
```

Start a new session after installation. If Claude asks you to reload plugins in the current session, follow that prompt.

The `btcp-skills` plugin includes financial-data connectors adapted from
[Anthropic's financial-services repository](https://github.com/anthropics/financial-services/tree/38652224c10610fa52eee2acee3ac712dcff01f2/plugins/vertical-plugins/financial-analysis)
under the Apache License 2.0. Connector access may require a provider subscription or authentication.

## Gallery actions

Each published skill exposes a one-off prompt, a versioned ZIP for Claude, and interface-specific instructions for installing the complete plugin.
