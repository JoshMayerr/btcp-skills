# BTCP skills

Portable Agent Skills for private equity and finance workflows from Beacon-Taylor Computational Partners.

## Install

Choose the package that fits how you want to work:

- **Complete collection:** install the `btcp-skills` plugin to get every published workflow plus its optional financial-data connectors.
- **One workflow:** install a standalone skill ZIP from the [BTCP skill gallery](https://beacontaylor.com/skills).
- **No installation:** copy a one-off prompt from the gallery into a new conversation.

Review the source and any connector permissions before installing a package.

### ChatGPT

ChatGPT does not currently document a self-service way to install an arbitrary plugin bundle from a ZIP file or GitHub repository URL. Do not upload `packages/plugins/btcp-skills.zip` as a ChatGPT plugin.

Plugins available to your account are installed from the Plugin Directory:

1. In ChatGPT on the web or desktop, select **Plugins** in the sidebar. You can also open your profile menu and select **Settings → Plugins**.
2. Open the plugin you want from the directory.
3. Select **Connect** when available and complete any required authorization.

For managed Business, Enterprise, or Edu workspaces, administrators control plugin availability and installation policy under **Workspace settings → Plugins**. Until the complete BTCP plugin is published to the directory or made available by your workspace administrator, use a standalone BTCP skill or a one-off prompt in ChatGPT.

#### Install one skill

1. Download the skill ZIP from the [BTCP skill gallery](https://beacontaylor.com/skills).
2. In the ChatGPT sidebar, select **Plugins**.
3. Select the **Skills** tab.
4. Select **Create → Upload from your computer**. The uploader accepts a `.zip` or `.skill` skill package, or a standalone `SKILL.md` file.
5. Wait for ChatGPT to scan the skill, review any warnings, and finish the installation.

Personal skills must be added separately on desktop and on web/mobile; they do not currently sync between those surfaces. OpenAI documents ZIP upload for [skills in ChatGPT](https://help.openai.com/en/articles/20001066), while its [plugin instructions](https://help.openai.com/en/articles/20001256) direct users to the Plugin Directory and workspace settings.

### Claude Cowork

#### Install one skill in Claude

1. Download its ZIP from the [BTCP skill gallery](https://beacontaylor.com/skills).
2. Open [Claude Skills](https://claude.ai/customize/skills).
3. Select **+ → Create skill → Upload a skill**, then choose the ZIP.

Uploaded custom skills are private to your account unless your Team or Enterprise workspace shares or provisions them.

#### Install the complete plugin in Cowork

1. Open **Settings → Plugins → Add plugin**.
2. Paste this repository URL:

   ```text
   https://github.com/JoshMayerr/btcp-skills
   ```

3. Select and install `btcp-skills`.

Your workspace administrator may need to allow the repository marketplace first.

### Codex

Register the marketplace and install the complete collection from a terminal:

```sh
codex plugin marketplace add JoshMayerr/btcp-skills
codex plugin add btcp-skills@btcp
```

Start a new Codex app task or CLI session after installation. Plugins are not currently supported in the Codex IDE extension.

To update later, refresh the marketplace, reinstall the plugin, and start a new session:

```sh
codex plugin marketplace upgrade btcp
codex plugin add btcp-skills@btcp
```

### Claude Code

Add the marketplace and install the complete collection:

```sh
claude plugin marketplace add JoshMayerr/btcp-skills
claude plugin install btcp-skills@btcp-skills
```

Start a new session after installation, or run `/reload-plugins` in an open session. To update later:

```sh
claude plugin marketplace update btcp-skills
claude plugin install btcp-skills@btcp-skills
```

### Rogo

Rogo does not publish a self-service import format for third-party Agent Skills. Copy a one-off prompt from the gallery into a new Rogo conversation and attach or select the relevant source material. For a governed workflow in Rogo's Prompt or Agent Library, ask your workspace administrator or Rogo implementation team to add it.

## What's included

The `btcp-skills` plugin includes every published skill in this repository. It also includes financial-data connectors adapted from [Anthropic's financial-services repository](https://github.com/anthropics/financial-services/tree/38652224c10610fa52eee2acee3ac712dcff01f2/plugins/vertical-plugins/financial-analysis) under the Apache License 2.0. Connector access may require a provider subscription or authentication.

Each published skill in the gallery includes a one-off prompt, a versioned standalone-skill ZIP, and platform-specific installation instructions.

## Develop and contribute

### Repository layout

- `skills/` is the canonical source for standalone, cross-agent skills.
- `drafts/` holds incomplete skills that are not installable or visible in the gallery.
- `catalog/skills.json` contains gallery metadata that does not belong in `SKILL.md`.
- `catalog/plugins.json` defines independently installable collections and agent packages.
- `catalog/agents.json` describes optional end-to-end agents built from canonical skills.
- `catalog/distribution.json` defines versioned source and release URLs used by generated prompts.
- `plugins/<plugin-name>/` contains generated skill bundles plus OpenAI and Claude manifests.
- `prompts/create/` contains copy-paste prompts for creating skills in ChatGPT.
- `prompts/create-claude/` contains the same prompts addressed to `/skill-creator` in Claude Cowork.
- `prompts/one-off/` contains copy-paste prompts for using supported workflows without installation.
- `packages/skills/` contains the versioned ZIP archives linked from the skill gallery.
- `packages/plugins/` receives generated plugin ZIP archives for release workflows.

Plugin folders stay flat because the OpenAI marketplace resolves them as `./plugins/<plugin-name>`. The catalog records whether each package is a collection or an agent.

### Add a skill

Create `skills/<skill-name>/SKILL.md` using lowercase kebab-case for the directory and frontmatter name. Keep the portable frontmatter limited to `name` and `description`, then add its gallery record to `catalog/skills.json`.

Keep incomplete work under `drafts/` with `status` set to `draft`. Move it to `skills/` and set `status` to `published` when it is ready. For a published skill, set `builderMode` to `self-contained`, `source-linked`, or `unavailable`, and set `promptMode` to `standalone`, `reduced`, or `unavailable`. A reduced one-off prompt must be authored at `prompts/reduced/<skill-name>.md`; the other public prompt files are generated.

To bundle skills for hosted products, add their names to a package in `catalog/plugins.json`. Do not edit generated copies under `plugins/*/skills/` directly.

Run `npm test` before publishing. It regenerates plugin bundles and gallery prompts before validation. Run `npm run package` to generate ZIP archives for every published skill and plugin.
