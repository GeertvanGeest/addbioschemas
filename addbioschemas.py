
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import yaml, json, shlex, re

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

            # ignore lines that are in between <!-- and --> as they are comments
            # Check for the start of a comment block
            if re.match(r"<!--", line):
                inside_comment_block = True
            
            # Check for the end of a comment block
            if re.match(r"-->", line):
                inside_comment_block = False

            # Check for the start of a code block
            if re.match(r"```", line):
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
                        key, value = opt.split("=")
                        opt_dict[key] = value.strip("'\"")
                    meta_file = opt_dict["file"]
                
                # load metadata file 
                with open(meta_file, 'r') as file:
                    if (meta_file.endswith(("yaml", "yml"))):
                        meta_dict = yaml.safe_load(file)
                    elif (meta_file.endswith("json")):
                        meta_dict = json.load(file)
                
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
