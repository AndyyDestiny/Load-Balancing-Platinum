s = int(input())
val = []
x_cor = []
y_cor = []
for i in range(s):
    val.append([eval(i) for i in input().split(" ")])

for i in val:
    x_cor.append(i[0])
    y_cor.append(i[1])

best_split = [0, 0]
x_plane = 0
y_plane = 0
for i in x_cor:
    split1 = 0
    split2 = 0
    for b in x_cor:
        if i + 1 > b:
            split1 += 1
        else:
            split2 += 1
    if abs(split1 - split2) < abs(best_split[0] - best_split[1]) or best_split[0] == 0:
        best_split[0] = split1
        best_split[1] = split2
        x_plane = i + 1

best_split = [0, 0]
for i in y_cor:
    split1 = 0
    split2 = 0
    for b in y_cor:
        if i + 1 > b:
            split1 += 1
        else:
            split2 += 1
    if abs(split1 - split2) < abs(best_split[0] - best_split[1]) or best_split[0] == 0:
        best_split[0] = split1
        best_split[1] = split2
        y_plane = i + 1

quads = [0, 0, 0, 0]
for i in range(len(x_cor)):
    if x_cor[i] > x_plane and y_cor[i] > y_plane:
        quads[0] += 1
    if x_cor[i] < x_plane and y_cor[i] > y_plane:
        quads[1] += 1
    if x_cor[i] < x_plane and y_cor[i] < y_plane:
        quads[2] += 1
    if x_cor[i] > x_plane and y_cor[i] < y_plane:
        quads[3] += 1

print(max(quads))
