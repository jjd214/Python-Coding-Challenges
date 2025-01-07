def main():

    sentence = input("Enter a sentence: ")

    def extract_words(input_str):
        words = []
        temp_word = ""

        for char in input_str:
            if char.isspace():
                words.append(temp_word)
                temp_word = ""
            else:
                temp_word += char

        if len(temp_word) > 0:
            words.append(temp_word)

        return words

    print(f"Extracted words: {extract_words(sentence)}")
main()
