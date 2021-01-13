#!/bin/python3

from codeforces import problem
from data_types import Supplier

class Codeforces(Supplier):
    # Tmp var to store last searched problem data
    problem_title = None
    problem_tlimit = None
    problem_memory_limit = None

    def __init__(self):
        self.url = "codeforces.com"
        self.name = "CodeForces"

    def getProblemSample(self, contest_id, index):
        title, time_limit, memory_limit, sample_tests = \
            problem.get_info(contest_id, index)
        self.problem_title = title
        self.problem_tlimit = time_limit
        self.problem_memory_limit = memory_limit
        return sample_tests

if __name__ == "__main__":
     contest_id = 1
     index = 'A'
     cf = Codeforces()

     sample_tests = cf.getProblemSample(contest_id, index)

     assert (cf.problem_title == 'A. Theatre Square')
     assert (cf.problem_tlimit == '1 second')
     assert (cf.problem_memory_limit == '256 megabytes')
     assert (list(sample_tests) == [('6 6 4', '4')])
