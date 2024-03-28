import json, os
from collections import deque


class ProcessNode:

    def __init__(self, json_inp):
        self.pid = json_inp['pid']
        self.name = json_inp['process_name']
        self.parent_pid = json_inp.get('parent_pid', None)
        self.children = json_inp.get('children', [])

    def __str__(self):
        return "%s (%d)" % (self.name, self.pid)


def load_data():
    with open(os.path.join(os.path.dirname(__file__), 'resources/process_info.json'), encoding="utf8") as f:
        processes = json.load(f)
        process_nodes = [ProcessNode(p) for p in processes]

        # Fill Children
        for p in process_nodes:
            p.children = [c for c in process_nodes if c.parent_pid == p.pid]
            # print(p)

        stack = deque()

        for p in process_nodes:
            if p.parent_pid is None:
                stack.append((p, 0))

        while len(stack) > 0:
            t = stack.pop()
            print('\t' * t[1] + str(t[0]))
            for pn in t[0].children:
                stack.append((pn, t[1] + 1))


def run():
    load_data()


# if __name__ == '__main__':
#    run()
