s = input()

check = [-1]*26

for i in range(len(s)):
    if check[ord(s[i])-97] != -1:
        continue
    else:
        check[ord(s[i])-97] = i

for i in range(26):
    print(check[i], end=' ')