import uuid

PEOPLE: map = {
    "Joao": {
        "fname": "Joao",
        "lname": "Silva"
    },
    "Maria": {
        "fname": "Maria",
        "lname": "Santos"
    },
    "Jose": {
        "fname": "Jose",
        "lname": "Carvalho"
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


def find_by_lname(lname: str) -> dict:
    return PEOPLE.get(lname, None)


def insert(person: map):
    if person['lname'] in PEOPLE:
        raise Exception('person already exists')

    PEOPLE[person['lname']] = {
        "lname": person['lname'],
        "fname": person["fname"]
    }


def remove(lname: str):
    PEOPLE.pop(lname, None)


def update(person: dict) -> bool:
    if find_by_lname(person['lname']):
        PEOPLE.update({
            person['lname']: {
                "lname": person["lname"],
                "fname": person["fname"]
            }
        })
        return True
    else:
        return False



