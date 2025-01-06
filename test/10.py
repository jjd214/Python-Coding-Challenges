def unique_characters(strng):
    strng = strng.lower()
    uniq_chars = {}
    for ch in strng:
        if ch in uniq_chars:
            uniq_chars[ch] += 1
        else:
            uniq_chars[ch] = 1
    return uniq_chars

input_string = input("Enter a string: ")
for k,v in unique_characters(input_string).items():
    print(f'{k} = {v}')