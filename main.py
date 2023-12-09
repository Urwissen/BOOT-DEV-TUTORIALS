print("Hello World")
path = "./books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()
    count_word = len(file_contents.split())
    print(count_word, "words found in the document")
    chars_in_count = {}
    for char in file_contents.lower():
        if char in chars_in_count and char.isalpha():
            chars_in_count[char] += 1
        elif char.isalpha():
            chars_in_count[char] = 1
    final = sorted(chars_in_count)
    for char in final:
        print(f"The '{char}' character was found {chars_in_count[char]} times")
