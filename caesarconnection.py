
from typing import Any, Optional
import requests

class CaesarAPI:
    CHARACTERISTICS_LISTS_ENDPOINT = "/Characteristics/GetCharacteristicsLists"
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

    def __init__(self, url: str, username: str, password: str) -> None:
        self.url = url
        self.session: requests.Session = self.login_and_create_session(username, password)
        if self.session is None:
            raise Exception("Failed to log in and create session.")
        
    def login_and_create_session(self, username: str, password: str) -> Optional[requests.Session]:
        session = requests.Session()
        login_url = f"{self.url}/account/login"
        login_data = {"Username": username, "Password": password}

        response = session.post(login_url, json=login_data)

        if response.ok:
            print("Successfully logged in and created session.")
            return session
        else:
            print(f"Failed to log in. Status code: {response.status_code}")
            return None
        
    def get_development(self) -> Optional[dict[str, Any]]:
        return self.get(self.DEVELOPMENT_X_MENU)
    
    def get_databases(self) -> Optional[dict[str, Any]]:
        return self.get(self.DATABASES_X_MENU)
    
    def get_methods(self) -> Optional[dict[str, Any]]:
        return self.get(self.METHODS_X_MENU)
    
    def get_technologies(self) -> Optional[dict[str, Any]]:
        return self.get(self.TECHNOLOGIES_X_MENU)
    
    def get_competences(self) -> Optional[dict[str, Any]]:
        return self.get(self.COMPETENCES_X_MENU)
        
    def get_os(self) -> Optional[dict[str, Any]]:
        return self.get(self.OS_X_MENU)
    
    def get_packages(self) -> Optional[dict[str, Any]]:
        return self.get(self.PACKAGES_X_MENU)
    
    def get_activities(self) -> Optional[dict[str, Any]]:
        return self.get(self.ACTIVITIES_X_MENU)
    
    def get_education(self) -> Optional[dict[str, Any]]:
        return self.get(self.EDUCATION_X_MENU)
    
    def get_experiences(self) -> Optional[dict[str, Any]]:
        return self.get(self.EXPERIENCES_X_MENU)
    
    def get(self, x_menu: str) -> Optional[dict[str, Any]]:
        headers = {
            "Accept": "application/json",
            "X-Menu": x_menu,
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.session.get(self.url + self.CHARACTERISTICS_LISTS_ENDPOINT, headers=headers)

        if response.ok:
            return response.json()
        else:
            print(f"Failed to retrieve characteristics lists. Status code: {response.status_code}, message: {response.text}")
            return None