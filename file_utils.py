import os


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
