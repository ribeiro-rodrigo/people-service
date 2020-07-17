from flask import request, make_response, abort
from repositories import people


def find_all():
    offset = request.args.get('offset', None)
    limit = request.args.get('limit', None)

    offset = int(offset) if offset else 0
    limit = int(limit) if limit else None

    people_list = people.find_all(offset=offset, limit=limit)

    return people_list


def find_one(id: str):
    person = people.find_by_id(id)

    if person:
        return person
    else:
        abort(404, "Person with last name {id} not found".format(id=id))


def create(person: map):
    try:

        people.insert(person)
        headers = {"Location": f"{person['lname']}"}
        return make_response("{lname} successfully created".format(lname=person['lname']), 201, headers)

    except:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=person['lname'])
        )


def update(id: str, person: map):
    person['id'] = id
    is_update = people.update(person)
    if is_update:
        return make_response("Person {lname} is updated".format(lname=person['lname']), 200)
    else:
        abort(404, "Person with last name {lname} not found".format(lname=person['lname']))


def remove(id: str):
    people.remove(id)
    return make_response("{id} successfully removed".format(id=id), 200)

