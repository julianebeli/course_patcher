import __init__
import os
from pathlib import Path


class Storer:
    def __init__(self, source_file='source.csv', store='record'):
        self.error_path = Path(__init__.here) / 'data' / 'error'
        Path.touch(self.error_path)

        self.source_path = Path(__init__.here) / 'data' / source_file
        self.store_path = Path(__init__.here) / 'data' / store

        self.processed: set(int) = self.setup(self.store_path)
        self.unprocessed: set(int) = self.get_source(self.source_path)
        self.jobs: list = self.diff()
        self.completed_jobs: int = 0

    def diff(self):
        return list(self.unprocessed - self.processed)

    def get_source(self, file):
        if not Path.exists(file):
            exit('No source data found')
        with open(file) as f:
            return set([int(y) for y in [x.strip().split(',')[0] for x in f.readlines()[1:]]])

    def setup(self, file):
        Path.touch(file)
        with open(file, 'r') as f:
            return set([int(y) for y in [x.strip() for x in f.readlines()] if y])

    def record(self, course_id):
        with open(self.store_path, 'a') as f:
            f.write(f"{course_id}\n")
        self.display_job_count()

    def report(self, api_result):
        with open(self.error_path, 'a') as f:
            msg = f"\n{api_result.method.params}\n{api_result.results[0]}\n"
            f.write(msg)
        self.display_job_count()

    def display_job_count(self):
        self.completed_jobs += 1
        remaining = len(self.jobs) - self.completed_jobs
        os.system('clear')
        print(f"{remaining} jobs to go ...")
