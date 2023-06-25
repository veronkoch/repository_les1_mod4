words = input(str())

def palindrom(words):
    return words == words[::-1]

print(palindrom(words))