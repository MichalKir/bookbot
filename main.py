import sys

def main():
    book_path = sys.argv[1]
    book_report(book_path)

def get_book_content(path):
    with open(path) as content:
        return content.read()

def count_words_in_book(book_content):
    return len(book_content.split())

def count_characters_in_book(book_content):
    characters_count = {}
    for character in book_content.lower():
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1
    return characters_count

def convert_characters_to_letters_list(characters_count):
    letter_list = []
    for character in characters_count:
        if character.isalpha():
            letter_list.append({"letter":character,"count":characters_count[character]})
    return letter_list

def sort_by_count(dict):
    return dict["count"]

def book_report(book_path):
    book_content = get_book_content(book_path)
    words_count = count_words_in_book(book_content)
    characters_in_book = count_characters_in_book(book_content)
    letters_list = convert_characters_to_letters_list(characters_in_book)
    letters_list.sort(reverse=True, key=sort_by_count)
    print(letters_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print(f"")
    for letter in letters_list:
        print(f"The {letter["letter"]} character was found {letter["count"]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()