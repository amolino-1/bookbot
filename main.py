def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Initalise word counter
        word_count = 0
        # Remove white space
        words = file_contents.split()

        # Count words
        for word in words:
            word_count += 1

        print(word_count)

if __name__ == "__main__":
    main()
