import requests

# External Configurations
GRAPHQL_ENDPOINT = "https://leetcode.com/graphql"
GRAPHQL_QUERY = "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"


def scrape_problem_data(problem_slug: str):
    response = requests.post(
        GRAPHQL_ENDPOINT,
        json={
            "operationName": "questionData",
            "variables": {"titleSlug": problem_slug},
            "query": GRAPHQL_QUERY,
        },
    )
    return response.json()


def extract_problem_details(response):
    question = response["data"]["question"]
    return {
        "question_id": question["questionFrontendId"],
        "title": question["title"],
        "content": question["content"],
        "url": f"https://leetcode.com/problems/{question['titleSlug']}/",
    }
