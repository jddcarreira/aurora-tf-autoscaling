import re

class Terraform(object):
    def __init__(self, project):
        self.project = project

    def change_n_nodes(self, vars_file, count):
        for l in open(self.project + vars_file, 'rw'):
            l = re.sub(r"(?i)^.*AURORA_NODES_COUNT.*$", "AURORA_NODES_COUNT = %s" % count, l)
            print l

    def get_n_nodes(self, vars_file):
        for l in open(self.project + "/" + vars_file, 'rw'):
            match = re.findall(r"^.*(AURORA_NODES_COUNT).*([\s\0-1][0-9])$", l)
        if match[0]:
            return match[0][1]
        return None

    def plan(self):
        pass

    def apply(self):
        pass
