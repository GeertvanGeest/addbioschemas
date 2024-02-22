from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import yaml, json

OCX_YAML_STARTER = "---"

SCRIPT_STARTER = '<script type="application/ld+json">\n'

class OCXMetadata(Extension):
    """Python-Markdown extension for adding bioschemas markup to HTML output."""

    def __init__(self, *args, **kwargs):
        # define config option for specifying JSON-LD context
        self.config = {"yaml": ["", "Specify yaml"]}
        super(OCXMetadata, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.md = md
        self.md.yaml = self.getConfig("yaml")
        md.preprocessors.register(OCXMetadataPreprocessor(md), "ocxmetadata", 28)


class OCXMetadataPreprocessor(Preprocessor):
    def run(self, lines):
        self.md.meta = None
        new_lines = []
        while lines:  # run through all the lines of md looking for YAML
            line = lines.pop(0)
            if line == "[add-bioschemas]":  # should be start of a YAML block
                yaml_file = self.md.yaml
                with open(yaml_file, 'r') as file:
                    bs_yaml = yaml.safe_load(file)
                new_line = (
                    SCRIPT_STARTER + json.dumps(bs_yaml, indent=4) + "\n</script>"
                )
                new_lines.append(new_line)
                self.md.meta = bs_yaml
            else:
                new_lines.append(line)
            
        return new_lines


def makeExtension(**kwargs):
    # allows calling of extension by string which is not dot-noted
    return OCXMetadata(**kwargs)
