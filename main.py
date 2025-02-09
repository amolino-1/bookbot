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

        return word_count

def char_count(book):
    my_dict = {}

    chars = book.lower()

    for char in chars:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1

    return my_dict


def main():
    print(word_count(book))
    print(char_count(book))

if __name__ == "__main__":
    main()
