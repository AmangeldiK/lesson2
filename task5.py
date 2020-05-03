while True:

    str1 = input('Enter text: ')
    length = len(str1)
    lower = 0
    upper = 0
    for item in str1:
        if item.islower():
            lower += 1
        elif item.isupper():
            upper += 1
    lower1 = round(lower/length * 100, 2)
    upper1 = round(upper/length * 100, 2)
    print(f'Percent of lowercase letters: {lower1}')
    print(f'Percent of uppercase letters: {upper1}')




















