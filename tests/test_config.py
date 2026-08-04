import markdown

TESTINPUT = '''
# awesome title
[add-bioschemas]
I started with some YAML and turned it into JSON-LD
'''


def test_metadata_from_extension_config():
    # metadata file is configured on the extension, not on the [add-bioschemas] tag
    md = markdown.Markdown(
        extensions=["addbioschemas"],
        extension_configs={"addbioschemas": {"metadata": "tests/metadata.yaml"}},
    )
    html = md.convert(TESTINPUT)

    assert '<script type="application/ld+json">' in html
    assert '"name": "ELIXIR Training Lesson template"' in html
    assert "[add-bioschemas]" not in html
