lst = []
for _ in range(5):
    a = list(map(int,(input().split())))
    lst.append(a)

for row in lst:
    for column in row:
        if column == 1:
            Row = lst.index(row)+1
            Column = row.index(column)+1
            print(abs(3-Row)+abs(3-Column))