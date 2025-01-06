def find_shortest_and_longest_words(input_string):
    words = input_string.split()

    shortest_length = len(words[0])
    longest_length = len(words[0])

    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length
        elif word_length > longest_length:
            longest_length = word_length
    
    shortest_words = []
    for word in words:
        if len(word) == shortest_length:
            shortest_words.append(word)

    shortest_words = ', '.join(shortest_words)

    longest_words = []
    for word in words:
        if len(word) == longest_length:
            longest_words.append(word)

    longest_words = ', '.join(longest_words)

    return f"Shortest Words: {shortest_words}\nLongest Words: {longest_words}"

input_string = input("Enter a string: ")
result = find_shortest_and_longest_words(input_string)
print(result)