import sys
from stats import wordCount, charCounter, sortedList

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    numWords = wordCount(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("-----------Word Count ----------")
    print(f"Found {numWords} total words")
    print("-------- Character Count -------")
    charCount = charCounter(text)
    # print(charCount)
    sortedDict = sortedList(charCount)
    for item in sortedDict:
        print(f"{item['char']}: {item['num']}")


def get_book_text(book):
    with open(book, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()

