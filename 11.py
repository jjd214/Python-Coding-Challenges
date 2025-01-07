def main():

    message = input("Enter message: ")

    def find_shortest_and_longest_word(input_string):
        words = input_string.split()
        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            else:
                longest_word = word

        return shortest_word, longest_word

    shortest, longest = find_shortest_and_longest_word(message)

    print(f"Longest word: {longest}\nShortest word: {shortest}")

main()
