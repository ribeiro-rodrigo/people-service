import uuid

PEOPLE: map = {
    "852b198ce56e11ea8c1228565aff1763": {
        "fname": "Joao",
        "lname": "Silva",
        "id": "852b198ce56e11ea8c1228565aff1763"
    },
    "952b1583236e11ea8c1228565a4f1743": {
        "fname": "Maria",
        "lname": "Santos",
        "id": "952b1583236e11ea8c1228565a4f1743"
    },
    "454b168ced6e41ea6c1228565aff1768": {
        "fname": "Jose",
        "lname": "Carvalho",
        "id": "454b168ced6e41ea6c1228565aff1768"
    }
}


def generate_id():
    return uuid.uuid4().hex


def find_all(offset: int = 0, limit=None) -> list:
    people_list = list(PEOPLE.values())

    if offset > len(people_list):
        return []

    offset = offset - 1 if 0 < offset else 0

    return people_list[offset:limit]


def find_by_id(id: str) -> dict:
    return PEOPLE.get(id, None)


def insert(person: map):

    id = generate_id()

    PEOPLE[id] = {
        "lname": person['lname'],
        "fname": person["fname"]
    }


def remove(id: str):
    PEOPLE.pop(id, None)


def update(person: dict) -> bool:
    if find_by_id(person['id']):
        PEOPLE.update({
            person[person['id']]: {
                "lname": person["lname"],
                "fname": person["fname"]
            }
        })
        return True
    else:
        return False



