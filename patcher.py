import __init__
from data_io import Storer
import json

from api.requestor2 import API


def update_license(course_id):
    params = {'methodname': 'update_course',
              'id': course_id,
              'course[license]': 'cc_by'}
    api.add_method(**dict(params))
    api.do()
    return api


def update_features(course_id):
    # /v1/courses/{course_id}/features/flags/{feature}
    params = {'methodname': 'set_feature_flag_courses',
              "course_id": course_id,
              "feature": "new_gradebook",
              "state": "on"}
    api.add_method(**params)
    api.do()
    return api


def patch_courses(course_id_list):
    for course in course_id_list:
        license = update_license(course)
        feature = update_features(course)

        if not (license.response_error or feature.response_error):
            storer.record(course)
        else:
            if license.response_error:
                storer.report(license)
            else:
                storer.report(feature)


if __name__ == "__main__":

    SERVER = 'prod'
    api = API(SERVER)

    SOURCE_DATA = 'source.csv'
    storer = Storer(source_file=SOURCE_DATA)

    patch_courses(storer.jobs)
