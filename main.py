with open("books/frankenstein.txt") as f:
    book = file_contents = f.read()

def word_count(book):

        # Initalise word counter
        word_count = 0
        # Remove white space
        words = file_contents.split()

        # Count words
        for word in words:
            word_count += 1

        print(word_count)

def char_count(book):
    my_dict = {}

    words = book.lower()

    for word in words:
        my_dict[word] = 0

    for word in words:
        my_dict[word] += 1

    print(my_dict)


def main():
    word_count(book)
    char_count(book)

if __name__ == "__main__":
    main()
