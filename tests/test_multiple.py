import markdown
from addbioschemas import addbioschemas

TESTINPUT = '''
# awesome title
[add-bioschemas file='tests/metadata.yaml']
I started with some YAML and turned it into JSON-LD
And I will add another json ld over here:
[add-bioschemas file='tests/metadata2.yaml']
'''

# no options given
md = markdown.Markdown(extensions = ["addbioschemas"])
print(md.convert(TESTINPUT))
