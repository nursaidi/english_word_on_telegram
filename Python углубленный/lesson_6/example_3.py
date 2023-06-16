from typing import List


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


def create_users_v1(first_names: list, last_names: list) -> list:
    users = []
    items = zip(first_names, last_names)
    for first_name, last_name in items:
        users.append(User(first_name, last_name))
    return users


def create_users_v2(first_names: List[str],
                    last_names: List[str]) -> List[User]:
    users = []
    items = zip(first_names, last_names)
    for first_name, last_name in items:
        users.append(User(first_name, last_name))
    return users
