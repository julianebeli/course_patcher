import __init__
from data_io import Storer

from api.requestor2 import API

storer = Storer()

api = API('beta')


def update_license(course_id):
    params = {'methodname': 'update_course', 'id': course, 'course[license]': 'cc_by'}
    api.add_method(**dict(params))
    api.do()
    return api.results


def patch_courses(course_id_list):
    for course in course_id_list:
        data = update_license(course)
        if not data.response_error:
            storer.record(course)
        else:
            storer.report(data)


if __name__ == "__main__":
    storer.record("3")
    storer.report("9")
    print(len(storer.source_data))
