row = int(input('Enter the number of rows '))

# Calculate the half of diamiond
if row % 2 == 0:
    half_rows = row // 2
else:
    half_rows = row // 2 + 1

# -------Upper part of the diamond-------
for i in range(1, half_rows + 1):
    # print spaces
    print(' ' * (half_rows - i), end='')
    num = 1
    for j in range(2 * i - 1):
        print(num, end='')
        num += 1
    print()

# -------Lower part of the diamond-------
for i in range(half_rows - 1, 0, -1):
    # print spaces
    print(' ' * (half_rows - i), end='')
    num = 1
    for j in range(2 * i - 1):
        print(num, end='')
        num += 1
    print()
