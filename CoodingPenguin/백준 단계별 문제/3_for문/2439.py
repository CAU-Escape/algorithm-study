import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    print((' ' * (cnt - i - 1) + ('*' * (i+1))))