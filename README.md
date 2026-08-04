# Adding bioschemas to mkdocs

A small markdown extension to add bioschemas to mkdocs. It requires a yaml or json file with bioschemas markup, and adds it to the rendered html. 

`addbioschemas` is a plain [Python-Markdown](https://python-markdown.github.io/) extension, so it also works with [Zensical](https://zensical.org/), the static site generator built by the Material for MkDocs team. Zensical reads `mkdocs.yml` directly and runs Python-Markdown extensions unchanged, so everything below applies to Zensical projects as-is — no separate configuration is needed.

## Installation

```bash
pip install addbioschemas
```

To use the plugin simply add `addbioschemas` to the list of plugins in `mkdocs.yml`:

```yml
markdown_extensions:
  - addbioschemas
```

## Usage

### Option 1: add the bioschemas file name to the markdown file

Simply add `[add-bioschemas file='path/to/yaml/metadata.yaml']` to the markdown file where you want to add the bioschemas. This method supports multiple metadata files. 

A markdown snippet of a page where you want to add bioschemas to:

```markdown
# awesome title
[add-bioschemas file='path/to/yaml/metadata.yaml']
I started with some YAML and turned it into JSON-LD
```

**Important**: If you are using [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), make sure there is markdown before the insertion of `[add-bioschemas]`. Otherwise, other plugins will add incorrect tags to the json-LD chunk. 

The contents of `path/to/yaml/metadata.yaml` use the bioschemas properties:

```yaml
"@context": https://schema.org/
"@type": LearningResource
"@id": https://elixir-europe-training.github.io/ELIXIR-TrP-LessonTemplate-MkDocs/
http://purl.org/dc/terms/conformsTo:
  "@type": CreativeWork
  "@id": https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE
description: Template for ELIXIR lessons
keywords: FAIR, OPEN, Bioinformatics, Teaching
name: ELIXIR Training Lesson template
# lookup at https://spdx.org/licenses/
license: CC-BY-4.0
author:
- "@type": Person
  name: Geert van Geest
  email: geert.vangeest@sib.swiss
  github: GeertvanGeest
  orcid: 0000-0002-1561-078X
- "@type": Person
  name: Elin Kronander
  github: elinkronander
  orcid: 0000-0003-0280-6318
```

`addbioschemas` also supports the json format. 

### Option 2: add the bioschemas file name to mkdocs.yml

Specify the path to the yaml file in `mkdocs.yml`. This method only supports one metadata file.

Add to `mkdocs.yml`:

```yaml
markdown_extensions:
  - addbioschemas:
      metadata: 'path/to/yaml/metadata.yaml'
```

A markdown snippet of a page where you want to add bioschemas to:

```markdown
# awesome title
[add-bioschemas]
I started with some YAML and turned it into JSON-LD
```


**Important**: If you are using [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), make sure there is markdown before the insertion of `[add-bioschemas]`. Otherwise, other plugins will add incorrect tags to the json-LD chunk. 

## Using with Zensical

[Zensical](https://zensical.org/) can read an existing `mkdocs.yml` file directly, and runs the same Python-Markdown extensions without changes, so both options above work in a Zensical project without modification — just install `addbioschemas` and keep your `mkdocs.yml` as is.

If you migrate a project to Zensical's native `zensical.toml` configuration instead, configure `addbioschemas` under its `markdown_extensions` setting the same way you would for any other Python-Markdown extension; see the [Zensical documentation](https://zensical.org/docs/setup/basics/) for the exact syntax.
