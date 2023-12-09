print("Hello World")
path = "./books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()
    count_word = len(file_contents.split())
    print(count_word)
    chars_in_count = {}
    for char in file_contents.lower():
        if char in chars_in_count:
            chars_in_count[char] += 1
        else:
            chars_in_count[char] = 1
    print(chars_in_count)
