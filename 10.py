def main():

    input_string = input("Enter a string: ")

    def unique_characters(input_str):
        strings = input_str.lower()
        unique_chars = {}

        for char in strings:
            if char in unique_chars:
                unique_chars[char] += 1
            else:
                unique_chars[char] = 1

        return unique_chars

    for key, value in unique_characters(input_string).items():
        print(f"{key} = {value}")
main()
