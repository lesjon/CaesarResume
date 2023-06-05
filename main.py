from datetime import date
import time
import dotenv
import os
import json
from typing import Any

import requests

from caesarconnection import CaesarAPI
from caesarparser import CaesarParser
import aws_secret

API_PATH = "https://portal.caesar.nl/api2"


def load_credentials() -> tuple[str, str]:
    """
    Get the credentials from the .env file, environment variables or from the aws secret manager
    """
    dotenv.load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    if username and password:
        return {'username': username, 'password': password}
    else:
        return aws_secret.get_secret()


def store_characteristics_lists(characteristics_lists: dict[str, Any]) -> None:
    with open("characteristics.json", "w") as json_out:
        json.dump(characteristics_lists, json_out)


def get_parsed_education(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_education()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_competences(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_competences()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_databases(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_databases()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_activities(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_activities()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_experiences(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_experiences()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_os(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_os()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_packages(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_packages()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_technologies(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_technologies()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_methods(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_methods()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_methods(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_methods()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_development(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_development()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_motivation(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    characteristics_lists = session.get_motivation()
    return [item for item in parser.parse_charachteristics_lists(characteristics_lists)]

def get_parsed_documents(
    session: CaesarAPI, parser: CaesarParser
) -> list[dict[str, str]]:
    documents_lists = session.get_documents()
    return [item for item in parser.parse_documents(documents_lists)]

def get_latest_document(
    session: CaesarAPI, parser: CaesarParser
) -> str:
    documents = get_parsed_documents(session, parser)
    sorted_documents = sorted(documents, key=lambda k: date.fromisoformat(k['Date']))
    return sorted_documents[-1]

def main():
    start = time.time()
    credentials = load_credentials()
    session = CaesarAPI(API_PATH, credentials)
    parser = CaesarParser()
    print("Education and Courses")
    for item in get_parsed_education(session, parser):
        print(f"item: {item}")
    print("Competences")
    for item in get_parsed_competences(session, parser):
        print(f"item: {item}")
    print("Databases")
    for item in get_parsed_databases(session, parser):
        print(f"item: {item}")
    print("Activities")
    for item in get_parsed_activities(session, parser):
        print(f"item: {item}")
    print("Experiences")
    for item in get_parsed_experiences(session, parser):
        print(f"item: {item}")
    print("OS")
    for item in get_parsed_os(session, parser):
        print(f"item: {item}")
    print("Packages")
    for item in get_parsed_packages(session, parser):
        print(f"item: {item}")
    print("Technologies")
    for item in get_parsed_technologies(session, parser):
        print(f"item: {item}")
    print("Methods")
    for item in get_parsed_methods(session, parser):
        print(f"item: {item}")
    print("Development")
    for item in get_parsed_development(session, parser):
        print(f"item: {item}")
    print("Motivation")
    for item in get_parsed_motivation(session, parser):
        print(f"item: {item}")
    document = get_latest_document(session, parser)
    print(f"item: {document}")
    resume_name, resume = session.download_document(document['Serial no.'])
    with open("resume.docx", "wb") as docx_out:
        docx_out.write(resume)
    end = time.time()
    print(f"Time taken: {end - start}")
    return end - start


if __name__ == "__main__":
    main()
