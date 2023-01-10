inputs = [
    "insert 2",
    "insert 5",
    "insert 3",
    "exists 2",
    "exists 4",
    "next 4",
    "prev 4",
    "delete 5",
    "next 4",
    "prev 4",
]

from sys import stdin

inputs, bb_tree = [item.split() for item in stdin.readlines()], []
for action, x in inputs:
    x = int(x)
    if "insert" in (action,) and x not in bb_tree:
        bb_tree.append(x)
    if "delete" in (action,) and x in bb_tree:
        bb_tree.remove(x)
    if "exists" in (action,):
        print("true" if x in bb_tree else "false")
    if "next" in (action,):
        bb_tree.sort()
        for e in bb_tree:
            if e > x:
                print(e)
                break
        else:
            print("none")
    if "prev" in (action,):
        bb_tree.sort()
        try:
            print([e for e in bb_tree if e < x][-1])
        except:
            print("none")
