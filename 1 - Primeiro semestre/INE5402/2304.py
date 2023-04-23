i, n = input().split()
i = int(i)
n = int(n)
l = [i, i, i]
for i in range(n):
    h = input().split()
    for i in range(len(h)):
        if h[i] == 'C':
            h[2] = int(h[2])
            if h[1] == 'D':
                l[0] = l[0] - h[2]
            if h[1] == 'E':
                l[1] = l[1] - h[2]
            if h[1] == 'F':
                l[2] = l[2] - h[2]
        if h[i] == 'V':
            h[2] = int(h[2])
            if h[1] == 'D':
                l[0] = l[0] + h[2]
            if h[1] == 'E':
                l[1] = l[1] + h[2]
            if h[1] == 'F':
                l[2] = l[2] + h[2]
        if h[i] == 'A':
            h[3] = int(h[3])
            if h[1] == 'D' and h[2] == 'E':
                l[0] = l[0] + h[3]
                l[1] = l[1] - h[3]
            if h[1] == 'D' and h[2] == 'F':
                l[0] = l[0] + h[3]
                l[2] = l[2] - h[3]
            if h[1] == 'E' and h[2] == 'D':
                l[1] = l[1] + h[3]
                l[0] = l[0] - h[3]
            if h[1] == 'E' and h[2] == 'F':
                l[1] = l[1] + h[3]
                l[2] = l[2] - h[3]
            if h[1] == 'F' and h[2] == 'D':
                l[2] = l[2] + h[3]
                l[0] = l[0] - h[3]
            if h[1] == 'F' and h[2] == 'E':
                l[2] = l[2] + h[3]
                l[1] = l[1] - h[3]
print(l[0]  , end=" ")
print(l[1]  , end=" ")        
print(l[2])