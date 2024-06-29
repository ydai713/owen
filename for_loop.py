"""
Format of for loop:

for var in iterable:
    <code block>
"""

# We are using range function as iterable

for i in range(5):  #  i = 0, 1, 2, 3, 4
    print(f"hello world {i}")


for i in range(3): # i = 0, 1, 2
    print(f"hello world {i}")


for i in range(8):  # i = 0, 1, 2, 3, 4, 5, 6, 7
    print(f"hello world {i}")


for i in range(2, 8):  # i = 2, 3, 4, 5, 6, 7
    print(f"hello world {i}")


# We are using string

for letter in "hello world":
    print(letter)

message = "good"
for letter in message:
    print(letter)
