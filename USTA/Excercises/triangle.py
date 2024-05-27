import sys

n = int(sys.argv[1])
num = 1

for i in range(n):
    type = "*"
    p = type * num
    num += 1
    print(p)
