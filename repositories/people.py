import uuid

PEOPLE: map = {
    "852b198ce56e11ea8c1228565aff1764": {
        "fname": "Joao",
        "lname": "Silva",
        "id": "852b198ce56e11ea8c1228565aff1764"
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


def insert(person: map) -> map:

    id = generate_id()

    person_inserted = {
        "lname": person['lname'],
        "fname": person["fname"],
        "id": id
    }

    PEOPLE[id] = person_inserted

    return person_inserted


def find_all(offset: int = 0, limit=None) -> list:
    people_list = list(PEOPLE.values())

    if offset > len(people_list):
        return []

    offset = offset - 1 if 0 < offset else 0

    return people_list[offset:limit]


def find_by_id(id: str) -> dict:
    return PEOPLE.get(id, None)


def remove(id: str):
    PEOPLE.pop(id, None)


def update(id: str, person: dict) -> bool:

    person_inserted = find_by_id(id)

    if person_inserted:
        person_inserted.update({"lname": person["lname"], "fname": person["fname"]})
        return True
    else:
        return False



