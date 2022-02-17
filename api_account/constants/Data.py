from enum import Enum


class RoleData(Enum):
    ADMIN = {
        "id": 1,
        "name": "ADMIN"
    }
    STUDENT = {
        "id": 2,
        "name": "STUDENT"
    }
    LECTURE = {
        "id": 3,
        "name": "LECTURE"
    }