import markdown

def read_from_md(file):
    with open(file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        return html
