import __init__
from data_io import Storer
import json

from api.requestor2 import API

api = API('beta')


def update_license(course_id):
    params = {'methodname': 'update_course', 'id': course_id, 'course[license]': 'cc_by'}
    api.add_method(**dict(params))
    api.do()
    return api


def patch_courses(course_id_list):
    for course in course_id_list:
        data = update_license(course)
        if not data.response_error:
            storer.record(course)
        else:
            storer.report(json.dumps(data.results, indent=4))


if __name__ == "__main__":
    storer = Storer(source_file='initial_source.csv')
    patch_courses(storer.jobs[:5])
