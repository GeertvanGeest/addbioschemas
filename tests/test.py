import markdown
from addbioschemas import OCXMetadata
TESTINPUT = '''
# awesome title
[add-bioschemas]
I started with some YAML and turned it into JSON-LD
'''
md = markdown.Markdown(
    extensions=["addbioschemas"],
    extension_configs={"addbioschemas": {"yaml": "metadata.yaml"}},
)
print(md.convert(TESTINPUT))
