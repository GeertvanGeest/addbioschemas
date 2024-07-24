import markdown
from addbioschemas import addbioschemas

TESTINPUT = '''
# awesome title
[add-bioschemas file='tests/metadata.json']
I started with some JSON and turned it into JSON-LD
'''

# no options given
md = markdown.Markdown(extensions = ["addbioschemas"])
print(md.convert(TESTINPUT))
