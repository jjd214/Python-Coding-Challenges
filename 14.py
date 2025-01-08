def main():

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    def are_anagrams(input_str1, input_str2):
        # clean both string by replacing all white spaces to non empty spaces and trans to lowercase
        cleaned_string1 = input_str1.replace("", " ").lower()
        cleaned_string2 = input_str2.replace("", " ").lower()

        # sort both clean string to check if it has same characters
        # returns True or False
        return sorted(cleaned_string1) == sorted(cleaned_string2)

    # check if func returns true / are anagrams
    if are_anagrams(str1, str2):
        print("Strings are anagrams")
    # 
    else:
        print("Strings are not anagrams")

main()
