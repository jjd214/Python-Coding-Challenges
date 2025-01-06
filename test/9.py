unique_char = ''
dup_char = ''
input_string = input('Enter your Msg: ')
for char in input_string:
    if char not in unique_char:
        unique_char += char
    else:
        dup_char += char
dup_char = set(dup_char)
dup_char = ''.join(dup_char)
print(f'Unique characters: {unique_char}\nDuplicate characters: {dup_char}')