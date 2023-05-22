from dotenv import load_dotenv
import os
import json
from typing import Any

from caesarconnection import CaesarAPI
from caesarparser import CaesarParser

load_dotenv()
url = "https://portal.caesar.nl/api2"
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


def store_characteristics_lists(characteristics_lists: dict[str, Any]) -> None:
    with open("characteristics.json", "w") as json_out:
        json.dump(characteristics_lists, json_out)

def main():
    session = CaesarAPI(url, username, password)
    parser = CaesarParser()
    print("Education and Courses")
    characteristics_lists = session.get_education()
    for item in parser.parse_charachteristics_lists(characteristics_lists):
        print(f"item: {item}")
    print("Competences")
    characteristics_lists = session.get_competences()
    for item in parser.parse_charachteristics_lists(characteristics_lists):
        print(f"item: {item}")
    print("Databases")
    characteristics_lists = session.get_databases()
    for item in parser.parse_charachteristics_lists(characteristics_lists):
        print(f"item: {item}")
    print("Activities")
    characteristics_lists = session.get_activities()
    for item in parser.parse_charachteristics_lists(characteristics_lists):
        print(f"item: {item}")
    print("Experiences")
    experience_lists = session.get_experiences()
    for item in parser.parse_charachteristics_lists(experience_lists):
        print(f"item: {item}")
    print("OS")
    os_lists = session.get_os()
    for item in parser.parse_charachteristics_lists(os_lists):
        print(f"item: {item}")
    print("Packages")
    package_lists = session.get_packages()
    for item in parser.parse_charachteristics_lists(package_lists):
        print(f"item: {item}")
    print("Technologies")
    technology_lists = session.get_technologies()
    for item in parser.parse_charachteristics_lists(technology_lists):
        print(f"item: {item}")
    print("Methods")
    method_lists = session.get_methods()
    for item in parser.parse_charachteristics_lists(method_lists):
        print(f"item: {item}")
    print("Development")
    development_lists = session.get_development()
    for item in parser.parse_charachteristics_lists(development_lists):
        print(f"item: {item}")

if __name__ == "__main__":
    main()
