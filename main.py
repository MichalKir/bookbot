import sys

def main():
    book_path = sys.argv[1]
    book_report(book_path)

def get_book_content(path):
    with open(path) as content:
        return content.read()

def count_words_in_book(content):
    return len(content.split())

def count_characters_in_book(content):
    char_count = {}
    for char in content.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def convert_character_count_to_letters_list(chars_count):
    letter_list = []
    for character in chars_count:
        if character.isalpha():
            letter_list.append({"letter":character,"count":chars_count[character]})
    return letter_list

def sort_by_count(dict):
    return dict["count"]

def book_report(book_path):
    book_content = get_book_content(book_path)
    words_count = count_words_in_book(book_content)
    chars_in_book = count_characters_in_book(book_content)
    letters_list = convert_character_count_to_letters_list(chars_in_book)
    letters_list.sort(reverse=True, key=sort_by_count)
    print(letters_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print(f"")
    for letter in letters_list:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()