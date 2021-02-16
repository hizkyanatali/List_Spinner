'''
awal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

akhir = [
    [],
    [],
    [],
    []
]

yang diinginkan:
akhir = [
    [4, 8, 12, 16],
    [3, 7, 11, 15],
    [2, 6, 10, 14],
    [1, 5, 9, 13]
]
akhir = [[4, 8, 12, 16],[3, 7, 11, 15],[2, 6, 10, 14],[1, 5, 9, 13]]
'''

print('~' * 20, "2. List Spinner", '~' * 20)


def ListSpinner():
    awal = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    akhir = [
        [],
        [],
        [],
        []
    ]
    for i in range(len(awal[0])):
        for j in range(len(awal[0])):
            akhir[i].append(awal[j][(len(awal[0]) - 1) - i])
    return akhir


print(ListSpinner())
