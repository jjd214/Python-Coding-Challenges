def are_anagrams(string1, string2):
    cleaned_string1 = string1.replace(" ", "").lower()
    cleaned_string2 = string2.replace(" ", "").lower()

    return sorted(cleaned_string1) == sorted(cleaned_string2)

input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

if are_anagrams(input_string1, input_string2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")