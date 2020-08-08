from flask import request, make_response, abort
from repositories import people


def read_all():
    offset = request.args.get('offset', None)
    limit = request.args.get('limit', None)

    offset = int(offset) if offset else 0
    limit = int(limit) if limit else None

    people_list = people.find_all(offset=offset, limit=limit)

    return people_list


def create(person: map):
    try:
        people.insert(person)
        return make_response("{lname} successfully created".format(lname=person['lname']), 201)
    except Exception:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=person['lname'])
        )

