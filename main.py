import sys
from stats import get_num_letter,get_num_each_letter,char_sort
def get_book_text(f):
	file_contents = f.read()
	return file_contents


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]

	with open(book_path, "r", encoding='utf-8') as f:
		t = get_book_text(f)
		num_words = get_num_letter(t)
		char_dict = get_num_each_letter(t)
		sorted = char_sort(char_dict)
		print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
		for dictionary in sorted:
			if dictionary['char'].isalpha():
				print(f"{dictionary['char']}: {dictionary['num']}")
		print(f"============= END ===============")


main()
