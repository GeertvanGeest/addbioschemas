# Adding bioschemas to mkdocs

A small markdown extension to add bioschemas to mkdocs. It requires a yaml or json file with bioschemas markup, and adds it to the rendered html. 

## Installation

```bash
pip install addbioschemas
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
