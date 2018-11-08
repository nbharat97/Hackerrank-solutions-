def timeConversion(s):
    s1 = str(10 * (int(s[0]) + 12) + int(s[1]))
    s2 = []
    s3 = str(s1)
    s2.append(s3)
    s2.extend(s[2:8])
    s = ''.join(s2)


s = input()
result = timeConversion(s)
print(result)
