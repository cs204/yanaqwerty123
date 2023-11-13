s = str(input())
for i in range(len(s)):
    if s[i].isupper():
        s = s.replace(s[i], '_' + s[i].lower())
print('Верблюжий стиль: ' + s)
