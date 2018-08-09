a = [9, 9]
b = [1]

# calculate 99 + 1 = 100 -> [0, 0, 1]
result = []
carry = 0
for i in range(max(len(a), len(b))):
    if i >= len(a):
        tmp = b[i] + carry
        if tmp >= 10:
            carry += 1
            result.append(tmp - 10)
        else:
            result[i] = tmp
    elif i >= len(b):
        tmp = a[i] + carry
        if tmp >= 10:
            carry += 1
            result.append(tmp - 10)
        else:
            result[i] = tmp
    else:
        tmp = b[i] + a[i]
        if tmp >= 10:
            carry += 1
            result.append(tmp - 10)
        else:
            result.append(tmp)

print(result)