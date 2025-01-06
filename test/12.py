# NOT USING SPLIT METHOD
def extract_words(input_string):
    words = []
    start_index = 0
    i = 0

    while i < len(input_string):
        char = input_string[i]

        if not char.isalnum():
            if start_index < i:
                words.append(input_string[start_index:i])
            start_index = i + 1

        i += 1

    if start_index < len(input_string):
        words.append(input_string[start_index:])

    return words

input_string = input("Enter a string: ")
result = extract_words(input_string)
print("Extracted words: \n", result)