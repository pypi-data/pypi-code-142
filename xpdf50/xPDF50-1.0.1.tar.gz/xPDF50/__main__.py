from PIL import Image
from xhtml2pdf import pisa
import argparse
import re
import requests


"""
    Given a url of a cs50's web page with a project, a problem or lecture notes
    xPDF50 returns a clean PDF file of the main content of that page.

"""

class Error:
    parser = argparse.ArgumentParser()

    @classmethod
    def exit(cls, message):
        cls.parser.exit(message)


def main():
    # User entered URL at the command-line
    if url := get_input():

        # Data related to user request
        course, year, material_name = unpack(url)

        # Altered html to get desired PDF
        html = modify_html(url, course, year, material_name)

        # Ship the pdf
        get_pdf(html, f"x{material_name.capitalize()}.pdf")


def get_input():
    """Gets input from user"""

    parser = argparse.ArgumentParser(prog='xPDF50')

    parser.add_argument(
        "url",
        type=str,
        help="url of a web page containing cs50's problem|project|notes",
    )

    args = parser.parse_args()

    if url := is_valid(args.url.lower()):
        return url

    else:
        Error.exit("hmm... looks like an invalid url    Try: project.py -h")


def is_valid(url):
    """If contains cs50's domain, return as a full url path"""

    if matches := re.search(
        r"^(?:https://)?(?:www\.)?(cs50.harvard.edu/.+)$",
        url,
    ):

        # Ensure that a full url path is returned
        return f"https://{matches.group(1)}".removesuffix("/")

    else:
        return False


def unpack(url):
    """Extract and match data from the url"""

    if "notes" in url:
        try:
            matches = re.search(
                r"^https://.+/(.+)/(\d\d\d\d)/notes/(\d)$",
                url,
            )
            course, year, lesson_number = (
                matches.group(1),
                matches.group(2),
                matches.group(3),
            )

        except (AttributeError):
            return handle_uncharted(url)
        else:
            return course, year, f"lecture{lesson_number}"

    elif "psets" in url or "projects" in url:
        try:
            matches = re.search(
                r"^https://.+/(.+)/(\d\d\d\d)/.+/\d/(.+)$",
                url,
            )
            course, year, problem_or_project_name = (
                matches.group(1),
                matches.group(2),
                matches.group(3),
            )

        except (AttributeError):
            return handle_uncharted(url)
        else:
            return course, year, f"{problem_or_project_name}"
    elif "project" in url:
        return handle_uncharted(url)
    else:
        Error.exit("Sorry... xPDF50 doesn't recognize this cs50 page     Try: project.py -h")



def handle_uncharted(url):
    """Handling data of unanticipated url with cs50.harvard.edu domain"""

    last_part = lambda path: path.split("/")[-1]

    return ".....", ".....", f"{last_part(url)}"


def modify_html(url, course, year, lesson):
    """Modify raw html to get desired PDF using xhtml2pdf module"""

    template = "<html><head><style>@page {size: a4 portrait;@frame content_frame {/* Content Frame */left: 50pt; width: 512pt; top: 50pt; height: 722pt;} @frame footer_frame { /* Another static Frame */-pdf-frame-content: footer_content;left: 376pt; width: 512pt; top: 792pt; height: 20pt;}}body{font-size: 10pt;}img {zoom: 70%;}code {font-family: Verdana;}</style></head><body>"
    content = extract_content(url)
    footer = f'<div id="footer_content">CS50/{course}/{year}/{lesson} (Page: <pdf:pagenumber>)</div>'

    return template + footer + content


def extract_content(url):
    """Extracting only the required content from html and convert it to a string"""

    try:
        html = requests.get(url, timeout=0.900)

        # Check if request response status is ok
        if html.status_code != requests.codes.ok:
            Error.exit("hmm... something is not right")

    except requests.exceptions.Timeout:
        Error.exit("cs50.harvard.edu took too long to respond")

    html = edit_tags(html.text, url)

    # Extracting from html's h1 tag onwards until </body> tag
    if matches := re.search(
        r'.+(<h1.+</body>).+',
        html,
        re.DOTALL,
    ):
        extracted_html = matches.group(1)

    return extracted_html.replace("â", "'")


def edit_tags(html, url):
    '''Remove or replace html tags to suit pdf format'''

    # Replace img src with full url path
    html = re.sub(r'<img.src="(.+)".alt=".+">', rf'<img src="{url}/\1">', html)

    # Removing video tags
    html = re.sub(r'<div class="ratio.+></iframe></div>', " ", html)

    # Removing demo
    html = re.sub(r'<h2.id="demo">Demo</h2>', " ", html)
    html = re.sub(r'<script async="".+</script>', " ", html
    )

    return html



def get_pdf(source_html, output_filename):
    """Convert html to a pdf file using xhtml2pdf module"""

    pisa.showLogging()

    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(source_html, dest=result_file)

    # close output file
    result_file.close()

    # return False on success and True on errors
    return pisa_status.err


if __name__ == "__main__":
    main()
