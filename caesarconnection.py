from typing import Any, Optional
import requests


class CaesarAPI:
    """
    Class for interacting with the Caesar API, getting information for your resume.
    """

    CHARACTERISTICS_LISTS_ENDPOINT = "/Characteristics/GetCharacteristicsLists"
    DOCUMENTS_ENDPOINT = "/Documents/GetDocumentsList"
    DEVELOPMENT_X_MENU = "9260"
    DATABASES_X_MENU = "9240"
    METHODS_X_MENU = "9250"
    TECHNOLOGIES_X_MENU = "9255"
    COMPETENCES_X_MENU = "9230"
    OS_X_MENU = "9270"
    PACKAGES_X_MENU = "9280"
    ACTIVITIES_X_MENU = "9290"
    EDUCATION_X_MENU = "9140"
    EXPERIENCES_X_MENU = "9130"
    MOTIVATION_X_MENU = "9120"
    DOCUMENTS_X_MENU = "9105"

    def __init__(self, url: str, credentials: dict[str, str]) -> None:
        self.url = url
        self.session: requests.Session = self.login_and_create_session(credentials)
        if self.session is None:
            raise Exception("Failed to log in and create session.")

    def login_and_create_session(
        self, credentials: dict[str, str]
    ) -> Optional[requests.Session]:
        session = requests.Session()
        login_url = f"{self.url}/account/login"

        response = session.post(login_url, json=credentials)

        if response.ok:
            print("Successfully logged in and created session.")
            return session
        else:
            print(f"Failed to log in. Status code: {response.status_code}")
            return None

    def get_development(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.DEVELOPMENT_X_MENU)

    def get_databases(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.DATABASES_X_MENU)

    def get_methods(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.METHODS_X_MENU)

    def get_technologies(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.TECHNOLOGIES_X_MENU)

    def get_competences(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.COMPETENCES_X_MENU)

    def get_os(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.OS_X_MENU)

    def get_packages(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.PACKAGES_X_MENU)

    def get_activities(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.ACTIVITIES_X_MENU)

    def get_education(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.EDUCATION_X_MENU)

    def get_experiences(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.EXPERIENCES_X_MENU)

    def get_motivation(self) -> Optional[dict[str, Any]]:
        return self.get_characteristics(self.MOTIVATION_X_MENU)

    def get_characteristics(self, x_menu: str) -> Optional[dict[str, Any]]:
        headers = {
            "Accept": "application/json",
            "X-Menu": x_menu,
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.session.get(
            self.url + self.CHARACTERISTICS_LISTS_ENDPOINT, headers=headers
        )

        if response.ok:
            return response.json()
        else:
            print(
                f"Failed to retrieve characteristics lists. Status code: {response.status_code}, message: {response.text}"
            )
            return None

    def get_documents(self, x_menu: str = DOCUMENTS_X_MENU) -> Optional[dict[str, Any]]:
        headers = {
            "Accept": "application/json",
            "X-Menu": x_menu,
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.session.get(self.url + self.DOCUMENTS_ENDPOINT, headers=headers)

        if response.ok:
            return response.json()
        else:
            print(
                f"Failed to retrieve characteristics lists. Status code: {response.status_code}, message: {response.text}"
            )
            return None

    def download_document(self, document_id: str, x_menu: str = DOCUMENTS_X_MENU
    ) -> Optional[bytes]:
        def parse_content_disposition(content_disposition: str) -> str:
            return content_disposition.split("filename=")[1].split(";")[0].replace('"', "")
        headers = {
            "Accept": "application/json",
            "X-Menu": x_menu,
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.session.get(
            self.url + f"/document/download/{document_id}", headers=headers
        )

        if response.ok:
            filename = parse_content_disposition(response.headers["Content-Disposition"])
            return filename, response.content
        else:
            print(
                f"Failed to download document. Status code: {response.status_code}, message: {response.text}"
            )
            return None
