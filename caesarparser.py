import json
from typing import Iterable, Any
import re

# function to merge two dictionaries, executin the merge function on the values when a key is present in both dictionaries
def _merge_two_dicts(x, y, merge_function):
    z = x.copy()
    z.update(y)
    for key in set(x).intersection(y):
        z[key] = merge_function(x[key], y[key])
    return z

class CaesarParser:
    """
    Parses the characteristics lists from Caesar API
    """
    def _get_fields_by_name_from_characteristics_lists(
        self, characteristics: dict[str, Any], field_names: set[str]
    ) -> Iterable[dict[str, str]]:
        def _remove_prefix_code(key: str) -> str:
            return re.sub(r"^\d{2}\.\d{4}\ ", "", key)

        educations = []
        field_defs = characteristics["list"]["set"]["fieldDefs"]
        for item in characteristics["list"]["items"]:
            education = dict()
            for field_def in field_defs:
                caption = field_def["caption"]
                if caption in field_names:
                    field_id = str(field_def["no"])
                    field = item["values"][field_id]["value"]
                    if caption == "Waarde":
                        field = _remove_prefix_code(field)
                    education = _merge_two_dicts(education, {caption: field}, lambda x, y: x +y)
            educations.append(education)
        return educations

    def parse_databases(self, item_list: dict[str, Any]) -> Iterable[tuple[str, str]]:
        return self.parse_default_characteristics_lists(item_list)

    def parse_competences(self, item_list: dict[str, Any]) -> Iterable[tuple[str, str]]:
        return self.parse_default_characteristics_lists(item_list)

    def parse_default_characteristics_lists(
        self, item_list: dict[str, Any]
    ) -> Iterable[dict[str, str]]:
        field_names = {"Waarde", "Level ( J / M / S / E )"}
        yield from self._get_fields_by_name_from_characteristics_lists(
            item_list, field_names
        )

    def parse_education(self, item_list: dict[str, Any]) -> Iterable[tuple[str, str]]:
        field_names = {
            "Profiel opl naam",
            "Profiel opl start",
            "Profiel opl eind",
            "Profiel opl diploma",
        }
        yield from self._get_fields_by_name_from_characteristics_lists(
            item_list, field_names
        )

    def parse_charachteristics_lists(
        self, characteristics_lists: list[dict[str, Any]]
    ) -> Iterable[tuple[str, str]]:
        for item_list in characteristics_lists:
            print(f"{item_list['caption']=}")
            match item_list["caption"]:
                case "Education":
                    yield from self.parse_education(item_list)
                case "Cursussen":
                    yield from self.parse_courses(item_list)
                case "Ervaringen":
                    yield from self.parse_experiences(item_list)
                case _:
                    yield from self.parse_default_characteristics_lists(item_list)

    def parse_courses(self, item_list: dict[str, Any]) -> Iterable[tuple[str, str]]:
        field_names = {
            "Value",
            "Profiel cur naam",
            "Profiel cur certificaat",
            "Profiel cur eind",
        }
        cursussen: list = self._get_fields_by_name_from_characteristics_lists(
            item_list, field_names
        )
        yield from cursussen

    def parse_experiences(self, item_list: dict[str, Any]) -> Iterable[tuple[str, str]]:
        field_names = {
            "Value",
            "Profiel ervaring klant",
            "Profiel ervaring branche",
            "Profiel ervaring datum vanaf",
            "Profiel ervaring datum tot",
            "Profiel ervaring functie",
            "Show on CV",
            "Profiel ervaring methoden",
            "Profiel ervaring technieken",
            "Profiel ervaring werkzaamheden",
        }
        yield from self._get_fields_by_name_from_characteristics_lists(
            item_list, field_names
        )
