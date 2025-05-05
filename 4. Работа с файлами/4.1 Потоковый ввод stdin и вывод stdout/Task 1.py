import sys
answer = [line.strip()[::-1] for line in sys.stdin]
print(answer)