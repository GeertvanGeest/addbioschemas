import markdown

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

# A single-line HTML comment must not be treated as an unterminated comment
# block, which would otherwise swallow the rest of the document.
TESTINPUT_SINGLE_LINE_COMMENT = '''
# awesome title
<!-- this is a comment -->
[add-bioschemas file='tests/metadata.yaml']
'''


def test_multiple_metadata_files_are_both_converted():
    # tests/metadata3.yaml and tests/metadata4.yaml don't exist: if these were
    # processed (instead of being skipped as inside a comment/code block),
    # this would raise FileNotFoundError.
    md = markdown.Markdown(extensions=["addbioschemas"])
    html = md.convert(TESTINPUT)

    assert html.count('<script type="application/ld+json">') == 2
    assert '"name": "ELIXIR Training Lesson template"' in html
    assert '"name": "Lesson template presentation"' in html

    # directives inside the comment and code block are left untouched
    assert "[add-bioschemas file='tests/metadata3.yaml']" in html
    assert "[add-bioschemas file='tests/metadata4.yaml']" in html


def test_single_line_comment_does_not_hide_later_directives():
    md = markdown.Markdown(extensions=["addbioschemas"])
    html = md.convert(TESTINPUT_SINGLE_LINE_COMMENT)

    assert '<script type="application/ld+json">' in html
    assert '"name": "ELIXIR Training Lesson template"' in html
