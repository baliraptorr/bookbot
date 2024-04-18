def main():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)

        letter_count = {}

        for word in words:
            for letter in word:
                letter = letter.lower()

                letter_count[letter] = letter_count.get(letter, 0) + 1

        print("--- Begin report of books/frankenstein.txt ---")

        letter_count = dict(
            sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        )

        for kulcs, elem in letter_count.items():
            print(f"The '{kulcs}' character was found {elem} times")


if __name__ == "__main__":
    main()
