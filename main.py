import os
import re
from datetime import datetime

import html2text
import requests


def get_problem_title_from_url(url):
    url_segments = url.split("/")
    return url_segments[4]  # The problem name is the fourth element


def build_markdown_title(question_id, problem_title, url):
    return f"""## [{question_id}. {problem_title}]({url}) \n\n"""


def convert_html_to_markdown(html_content):
    text_maker = html2text.HTML2Text()
    # Configure options as needed
    text_maker.ignore_links = False
    text_maker.bypass_tables = False

    markdown_text = text_maker.handle(html_content)
    return markdown_text


def replace_asterisk_enclosed_words(text):
    pattern = r"\*\*(Input:|Output:|Explanation:)\*\*"
    return re.sub(pattern, r"\1", text)


def replace_image_placeholder(text):
    return text.replace("![]", "![image]")


def modify_markdown_details(markdown_raw):
    markdown_text = replace_asterisk_enclosed_words(markdown_raw)
    markdown_text = replace_image_placeholder(markdown_text)
    return markdown_text


def format_content_to_markdown(question_id, problem_title, content, url):
    title = build_markdown_title(question_id, problem_title, url)
    markdown_raw = convert_html_to_markdown(content)
    markdown_text = modify_markdown_details(markdown_raw)
    return title + markdown_text


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def write_file(file_name, content):
    if content is None:
        create_file(file_name)
    else:
        create_and_write_file(file_name, content)


def create_and_write_file(file_name, content):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)


def create_file(file_name):
    open(file_name, "w").close()


def query_leetcode_graphql(problem_name: str):
    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": problem_name},
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n",
    }

    return requests.post("https://leetcode.com/graphql", json=data).json()


def extract_problem_data(response):
    return {
        "question_id": response["data"]["question"]["questionFrontendId"],
        "problem_title": response["data"]["question"]["title"],
        "content": response["data"]["question"]["content"],
    }


def fetch_leetcode_problem_data(url):
    problem_name = get_problem_title_from_url(url)
    query = query_leetcode_graphql(problem_name)
    problem_data = extract_problem_data(query)
    problem_data.update({"url": url})

    return problem_data


def build_parent_directory_name(problem_title: str):
    today_formatted = datetime.today().strftime("%Y-%m-%d")
    parent_directory_name = (
        f"questions/{today_formatted}_{problem_title.replace(' ', '-')}"
    )
    return parent_directory_name


def build_problem_files(problem_data: dict):
    parent_directory_name = build_parent_directory_name(problem_data["problem_title"])
    create_directory(parent_directory_name)

    problem_files = [
        {
            "file_name": f"{parent_directory_name}/README.md",
            "content": format_content_to_markdown(**problem_data),
        },
        {"file_name": f"{parent_directory_name}/solution.py", "content": None},
    ]

    for problem_file in problem_files:
        write_file(**problem_file)

    return [problem_file["file_name"] for problem_file in problem_files]


def main():
    url = input("Enter the LeetCode problem URL: ")

    problem_data = fetch_leetcode_problem_data(url)
    problem_files = build_problem_files(problem_data)
    print("Successfully created the following files:\n" + "\n".join(problem_files))


if __name__ == "__main__":
    main()
