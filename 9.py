def main():
    unique_char = ""
    dup_char = ""

    input_str = input("Enter message: ")

    for char in input_str:
        if char not in unique_char:
            unique_char += char
        else:
            dup_char +=char

    dup_char = set(dup_char)
    dup_char = "".join(dup_char)

    print(f"Unique characters: {unique_char}")
    print(f"Duplicate characters: {dup_char}")

main()
