import numpy
import json

def task(json_tree:str)->list[list]:
    ans = [
        [],
        [],
        [],
        [],
        []
    ]
    tree = json.loads(json_tree)
    for i in range(len(tree)):
        if len(tree[i]) > 0:
            ans[0].append(i)

    for i in range(len(tree) - 1):
         ans[1].append(i + 1)

    for i in range(len(tree)):
        if len(tree[i]) == 0:
            pass
        has_grandchild = False
        for j in range(len(tree[i])):
            if len(tree[tree[i][j]]) > 0:
                has_grandchild = True
                break
        if has_grandchild:
            ans[2].append(i)

    for i in range(len(tree)):
        if i not in tree[0] and i != 0:
            ans[3].append(i)

    for i in range(len(tree)):
        if len(tree[i]) > 1:
            for j in range(len(tree[i])):
                ans[4].append(tree[i][j])


    return ans

tree = [
    [1, 2, 3],
    [5, 6],
    [7],
    [8],
    [],
    [],
    [],
    [],
    []
]
print(task(json_tree=json.dumps(tree)))


