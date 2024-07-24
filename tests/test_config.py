import markdown
from addbioschemas import addbioschemas
TESTINPUT = '''
# awesome title
[add-bioschemas]
I started with some YAML and turned it into JSON-LD
'''

md = markdown.Markdown(
    extensions = ["addbioschemas"],
    extension_configs = {"addbioschemas": {"metadata" : "tests/metadata.yaml"}}
)
print(md.convert(TESTINPUT))

