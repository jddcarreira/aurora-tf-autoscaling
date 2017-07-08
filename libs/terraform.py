import re


class Terraform(object):
    def __init__(self, project):
        self.project = project

    def change_n_nodes(self, vars_file, count):
        for l in open(self.project + vars_file, 'rw'):
            l = re.sub(r"(?i)^.*AURORA_NODES_COUNT.*$", "AURORA_NODES_COUNT = %s" % count, l)
            print l

    def get_n_nodes(self, vars_file):
        print vars_file
        return 2

    def plan(self):
        pass

    def apply(self):
        pass