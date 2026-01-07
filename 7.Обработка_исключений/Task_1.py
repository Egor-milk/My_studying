import sys


summary = 0
not_int = 0
for i in sys.stdin.read().split():
    try:
        summary += int(i)
    except ValueError:
        not_int += 1
print(summary)
print(not_int)