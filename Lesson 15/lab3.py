def output_str(tag):

    def inner(s):
        print(f"<{tag}>{s}</{tag}>")

    return inner


html_text = output_str("h1")
html_text("Hello world")
