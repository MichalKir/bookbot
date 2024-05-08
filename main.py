import sys

def main():
    book_path = sys.argv[1]
    book_content = get_book_content(book_path)
    words = count_words_in_book(book_content)
    characters_in_book = count_characters_in_book(book_content)
    print(characters_in_book)

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

if __name__ == "__main__":
    main()