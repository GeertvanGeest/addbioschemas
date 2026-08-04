import markdown

TESTINPUT = '''
# awesome title
[add-bioschemas file='tests/metadata.json']
I started with some JSON and turned it into JSON-LD
'''


def test_metadata_from_json_file():
    # no metadata configured on the extension, file is given on the [add-bioschemas] tag
    md = markdown.Markdown(extensions=["addbioschemas"])
    html = md.convert(TESTINPUT)

    assert '<script type="application/ld+json">' in html
    assert '"name": "ELIXIR Training Lesson template"' in html
    assert "[add-bioschemas" not in html
