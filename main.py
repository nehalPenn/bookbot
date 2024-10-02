def main():
    get_book = 'books/frankenstein.txt'
    f = open(get_book, "r")
    lines = f.read()
    words = lines.split()
    # print(len(words))
    word_length = len(words)
    letter_dict = {}
    for word in words:
        for c in word:
            c = c.lower()
            if c.isalpha():
                letter_dict[c] = letter_dict.get(c, 0) + 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_length} words found in the document")
    for key in letter_dict:
        print(f"The '{key}' character was found {letter_dict[key]} times")

    

main()