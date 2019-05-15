import __init__
from pathlib import Path


class Storer:
    def __init__(self, source_file='source.csv', store='store.py'):
        self.source_path = Path(__init__.here) / source_file
        self.store_path = Path(__init__.here) / store
        self.counted_courses: set(int) = self.setup()
        self.source_data: set(int) = self.get_source()

    def diff(self):
        return self.source_data - self.counted_courses

    def get_source(self):
        with open('initial_source.csv') as f:
            data = set([int(y) for y in [x.strip().split(',')[0] for x in f.readlines()[1:]]])
        return data

    def setup(self):
        with open(self.store_path, 'r') as f:
            d = f.read()
            if d:
                print("stored data found")
                process(d)
                return set()
            else:
                print("no data")
                return set()

    def record(self, course_id):
        print(f"adding {course_id} to record")

    def report(self, api_result):
        print(api_result)

# what's wrong here? It needs to handle the data stream breaking down
