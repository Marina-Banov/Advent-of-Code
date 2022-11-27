# PERT diagram with no costs taken into consideration, prioritizing alphabetically

from operator import attrgetter


class Task:
    def __init__(self, name, dependencies=[]):
        self.name = name
        self.dependencies = dependencies

    def __str__(self):
        return self.name


def critical_path(remaining):
    completed = []

    while len(remaining) > 0:
        i = 0
        while i < len(remaining):
            if all(elem in completed for elem in remaining[i].dependencies):
                completed.append(remaining[i])
                remaining.remove(remaining[i])
                i = -1
            i += 1

    return completed


def main():
    f = open("input.txt", 'r')

    all_tasks = []
    while True:
        line = f.readline()
        if line == "":
            break
        dep = next((t for t in all_tasks if t.name == line[5]), None)
        if dep is None:
            dep = Task(line[5], [])
            all_tasks.append(dep)
        cur = next((t for t in all_tasks if t.name == line[36]), None)
        if cur is not None:
            cur.dependencies.append(dep)
        else:
            all_tasks.append(Task(line[36], [dep]))

    res = ""
    for t in critical_path(sorted(all_tasks, key=attrgetter("name"))):
        res = res + str(t)
    print(res)


if __name__ == "__main__":
    main()
