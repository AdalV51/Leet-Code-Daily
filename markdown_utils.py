import re

import html2text


def html_to_markdown(html_content):
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.bypass_tables = False
    return converter.handle(html_content)


def format_markdown(question_id, title, content, url):
    markdown_title = f"## [{question_id}. {title}]({url}) \n\n"
    markdown_content = html_to_markdown(content)
    markdown_content = clean_up_markdown(markdown_content)
    return markdown_title + markdown_content


def clean_up_markdown(text):
    text = re.sub(r"\*\*(Input:|Output:|Explanation:)\*\*", r"\1", text)
    return text.replace("![]", "![image]")
