set1 = """
Set 1
 1  3  5  7
 9 11 13 15
17 19 21 23
25 27 29 31
"""
set2 = """
Set 2
 2  3  6  7
10 11 14 15
18 19 22 23
26 27 30 31
"""
set3 = """
Set 3
 4  5  6  7
12 13 14 15
20 21 22 23
28 29 30 31
"""
set4 = """
Set 4
 8  9 10 11
12 13 14 15
24 25 26 27
28 29 30 31
"""
set5 = """
Set 5
16 17 18 19
20 21 22 23
24 25 26 27
28 29 30 31
"""

day = 0

print(set1)
answer = input("Is your birthday in set 1?(y/n): ")
if answer == 'y':
    day += 1

print(set2)
answer = input("Is your birthday in set 2?(y/n): ")
if answer == 'y':
    day += 2

print(set3)
answer = input("Is your birthday in set 3?(y/n): ")
if answer == 'y':
    day += 4

print(set4)
answer = input("Is your birthday in set 4?(y/n): ")
if answer == 'y':
    day += 8

print(set5)
answer = input("Is your birthday in set 5?(y/n): ")
if answer == 'y':
    day += 16

print("\nYour birthday is",day)

sets = [
    (1, "Set 1\n 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31"),
    (2, "Set 2\n 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31"),
    (4, "Set 3\n 4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31"),
    (8, "Set 4\n 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31"),
    (16, "Set 5\n16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31"),
]

day = sum(value for value, text in sets if input(f"{text}\nIs your birthday in this set? (y/n): ") == 'y')
print("\nYour birthday is", day)
