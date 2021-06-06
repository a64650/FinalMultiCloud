def ceaseren(StringInput, key):
    result = ""
    for char in StringInput:
        if char.isupper():
            result += chr((ord(char) + (key-65)) % 26 + 65)
        else:
            result += chr((ord(char) + (key - 97)) % 26 + 97)
    return result


def ceaserdec(StringInput, key):
    key = int(key) % 26
    return ceaseren(StringInput, 26-key)


print(ceaseren("abc", 1))
print(ceaserdec("bcd", 1))
