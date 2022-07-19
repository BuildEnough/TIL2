word_list = ['abc', 'banana', 'apple']


def transform_uppercase(word):
    result = ''
    for char in word:
        number = ord(char)
        number = number - 32
        result += char(number)
    return result

for word in word_list:
    print(transform_uppercase(word))