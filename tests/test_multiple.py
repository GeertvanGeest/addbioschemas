import markdown
from addbioschemas import addbioschemas

TESTINPUT = '''
# awesome title
[add-bioschemas file='tests/metadata.yaml']
I started with some YAML and turned it into JSON-LD
And I will add another json ld over here:
[add-bioschemas file='tests/metadata2.yaml']

<!-- 
[add-bioschemas file='tests/metadata3.yaml']
-->

```python
a = 1
[add-bioschemas file='tests/metadata4.yaml']
```

'''


# # read TESTINPUT line by line
# lines = TESTINPUT.split('\n')

# new_lines = []

# while lines:  # run through all the lines of md looking for [add-bioschemas]å
#     if re.match(r"```", lines[0]):
#         while not re.match(r"```", lines[0]):
#             new_lines.append(lines.pop(0))
#         new_lines.append(lines.pop(0))
#         continue

#     new_lines.append('00000' + lines.pop(0))

# no options given
md = markdown.Markdown(extensions = ["addbioschemas"])
print(md.convert(TESTINPUT))
