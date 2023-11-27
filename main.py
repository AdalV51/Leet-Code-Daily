import os
from datetime import datetime

from file_utils import create_directory, write_file
from leetcode_scraper import extract_problem_details, scrape_problem_data
from markdown_utils import format_markdown


def get_problem_slug_from_url(url):
    return url.split("/")[4]


def build_directory_name(title: str):
    date_str = datetime.today().strftime("%Y-%m-%d")
    safe_title = title.replace(" ", "-")
    return os.path.join("questions", f"{date_str}_{safe_title}")


def generate_problem_files(problem_data):
    directory_name = build_directory_name(problem_data["title"])
    create_directory(directory_name)

    markdown_content = format_markdown(**problem_data)
    write_file(os.path.join(directory_name, "README.md"), markdown_content)
    write_file(os.path.join(directory_name, "solution.py"), None)

    return directory_name


def main():
    url = input("Enter the LeetCode problem URL: ")
    problem_slug = get_problem_slug_from_url(url)
    response = scrape_problem_data(problem_slug)
    problem_data = extract_problem_details(response)
    directory_name = generate_problem_files(problem_data)
    print(f"Files generated in {directory_name}")


if __name__ == "__main__":
    main()
