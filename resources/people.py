from flask import request
from repositories import people


def read_all():
    offset = request.args.get('offset', None)
    limit = request.args.get('limit', None)

    offset = int(offset) if offset else 0
    limit = int(limit) if limit else None

    people_list = people.find_all(offset=offset, limit=limit)

    return people_list

def create():
    pass

