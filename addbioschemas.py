
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import json
import shlex
import yaml

class addbioschemas(Extension):
    """Python-Markdown extension for adding bioschemas markup to HTML output."""

    def __init__(self, *args, **kwargs):
        # define config option for specifying metadata file
        self.config = {"metadata": ["", "Specify a metadata files"]}
        super(addbioschemas, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.md = md
        # should be a dict
        self.md.metadata = self.getConfig("metadata")
        md.preprocessors.register(
            addbioschemasPreprocessor(md),
            "addbioschemas",
            28
            )

class addbioschemasPreprocessor(Preprocessor):
    def run(self, lines):

        self.md.meta = None
        new_lines = []
        inside_comment_block = False
        inside_code_block = False

        while lines:  # run through all the lines of md looking for [add-bioschemas]

            line = lines.pop(0)

            # ignore lines that are in between <!-- and --> as they are comments.
            # A line that opens and closes the comment on its own (e.g. "<!-- foo -->")
            # must not flip the state permanently.
            has_open = "<!--" in line
            has_close = "-->" in line
            if has_open and not has_close:
                inside_comment_block = True
            elif has_close:
                inside_comment_block = False

            # Check for the start/end of a code block
            if line.startswith("```"):
                inside_code_block = not inside_code_block

            # If not inside a comment or code block, perform the replacement
            if line.startswith("[add-bioschemas") and not inside_comment_block and not inside_code_block:
                trimmed_string = line.strip("[]")
                # splits correctly based on spaces within quotes
                options = shlex.split(trimmed_string)

                if len(options) == 1:
                    # if no file is specified, use the default metadata file specified in the config
                    meta_file = self.md.metadata
                else:
                    # if file is specified, use that and parse other options
                    # removes add-bioschemas
                    options = options[1:]
                    opt_dict = {}
                    for opt in options:
                        key, value = opt.split("=", 1)
                        opt_dict[key] = value.strip("'\"")
                    if "file" not in opt_dict:
                        raise ValueError(
                            "[add-bioschemas] requires a 'file' option, "
                            "e.g. [add-bioschemas file='path/to/metadata.yaml']"
                        )
                    meta_file = opt_dict["file"]

                # load metadata file
                with open(meta_file, "r", encoding="utf-8") as file:
                    if meta_file.endswith(("yaml", "yml")):
                        meta_dict = yaml.safe_load(file)
                    elif meta_file.endswith("json"):
                        meta_dict = json.load(file)
                    else:
                        raise ValueError(
                            f"Unsupported metadata file format: '{meta_file}'. "
                            "Use a .yaml, .yml or .json file."
                        )

                new_line = (
                    '<script type="application/ld+json">\n' + json.dumps(meta_dict, indent=4) + "\n</script>"
                )
                new_lines.append(new_line)
                self.md.meta = meta_dict
            else:
                new_lines.append(line)
        return new_lines


def makeExtension(**kwargs):
    # allows calling of extension by string which is not dot-noted
    return addbioschemas(**kwargs)
