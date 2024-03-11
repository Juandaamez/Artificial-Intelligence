import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
result = lambda a, b: a * b

print(f'The result is: {result(a, b)}')