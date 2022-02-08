numbers_line1 = input().split()
numbers_line2 = input().split()

answer = map(lambda x, y: int(x) ^ int(y), numbers_line1, numbers_line2)
print(*answer, sep=' ')
