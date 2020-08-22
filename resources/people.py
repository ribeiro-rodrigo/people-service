from flask import request, make_response, abort
from repositories import people


def find_all():
    offset = request.args.get('offset', None)
    limit = request.args.get('limit', None)

    offset = int(offset) if offset else 0
    limit = int(limit) if limit else None

    people_list = people.find_all(offset=offset, limit=limit)

    return people_list


def find_by_lname(lname):
    person = people.find_by_lname(lname)

    if person:
        return person
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))


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


def update(lname, person):
    is_update = people.update(person)
    if is_update:
        return make_response("Person {lname} is updated".format(lname=person['lname']), 200)
    else:
        abort(404, "Person with last name {lname} not found".format(lname=person['lname']))


def remove(lname: str):
    people.remove(lname)
    return make_response("{lname} successfully removed".format(lname=lname), 200)

