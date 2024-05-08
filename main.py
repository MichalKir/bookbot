import sys

def main():
    book_path = sys.argv[1]
    book_content = get_book_content(book_path)
    print(count_words_in_book(book_content))

def get_book_content(path):
    with open(path) as content:
        return content.read()

def count_words_in_book(book_content):
    return len(book_content.split())

if __name__ == "__main__":
    main()