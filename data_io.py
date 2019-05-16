import __init__
from pathlib import Path


class Storer:
    def __init__(self, source_file='source.csv', store='record'):
        self.error_path = Path(__init__.here) / 'data' / 'error'
        Path.touch(self.error_path)

        self.source_path = Path(__init__.here) / 'data' / source_file
        self.store_path = Path(__init__.here) / 'data' / store

        self.processed: set(int) = self.setup(self.store_path)
        self.unprocessed: set(int) = self.get_source(self.source_path)
        self.jobs = self.diff()

    def diff(self):
        return list(self.unprocessed - self.processed)

    def get_source(self, file):
        if not Path.exists(file):
            exit('No source data found')
        with open(file) as f:
            data = set([int(y) for y in [x.strip().split(',')[0] for x in f.readlines()[1:]]])
        return data

    def setup(self, file):
        Path.touch(file)
        with open(file, 'r') as f:
            data = set([int(y) for y in [x.strip() for x in f.readlines()] if y])
            return data

    def record(self, course_id):
        print(f"adding {course_id} to record")
        with open(self.store_path, 'a') as f:
            f.write(f"{course_id}\n")

    def report(self, api_result):
        print(api_result)
        with open(self.error_path, 'a') as f:
            f.write(f"{api_result}\n")
