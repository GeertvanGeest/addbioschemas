from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import yaml, json

class addbioschemas(Extension):
    """Python-Markdown extension for adding bioschemas markup to HTML output."""

    def __init__(self, *args, **kwargs):
        # define config option for specifying yaml file
        self.config = {"yaml": ["", "Specify yaml"]}
        super(addbioschemas, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.md = md
        self.md.yaml = self.getConfig("yaml")
        md.preprocessors.register(addbioschemasPreprocessor(md), "addbioschemas", 28)


class addbioschemasPreprocessor(Preprocessor):
    def run(self, lines):
        self.md.meta = None
        new_lines = []
        while lines:  # run through all the lines of md looking for [add-bioschemas]
            line = lines.pop(0)
            if line == "[add-bioschemas]":  
                yaml_file = self.md.yaml
                with open(yaml_file, 'r') as file:
                    bs_yaml = yaml.safe_load(file)
                new_line = (
                    '<script type="application/ld+json">\n' + json.dumps(bs_yaml, indent=4) + "\n</script>"
                )
                new_lines.append(new_line)
                self.md.meta = bs_yaml
            else:
                new_lines.append(line)
            
        return new_lines


def makeExtension(**kwargs):
    # allows calling of extension by string which is not dot-noted
    return addbioschemas(**kwargs)
