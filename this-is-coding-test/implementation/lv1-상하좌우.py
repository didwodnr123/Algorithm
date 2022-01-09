n = int(input())
commands = input().split()

x, y = 1, 1
cmd_map = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}

for cmd in commands:
    dx, dy = cmd_map[cmd]
    if x + dx < 1 or x + dx > n or y + dy < 1 or y + dy > n:
        continue
    x += dx
    y += dy

print(x, y)
