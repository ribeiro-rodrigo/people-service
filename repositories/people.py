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


def find_all(offset: int = 0, limit=None) -> list:
    people_list = list(PEOPLE.values())

    if offset > len(people_list):
        return []

    offset = offset - 1 if 0 < offset else 0

    return people_list[offset:limit]


