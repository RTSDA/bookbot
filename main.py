from collections import Counter

def count_characters(text):
	if text is None:
		return None
	text = text.lower()
	char_count= Counter(c for c in text if c.isalpha())
	return dict(char_count)
def main():
	with open("/Users/benjaminslingo/Development/github/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read()
		char_count = count_characters(file_contents)
		words = file_contents.split()
		word_count = len(words)
		#print(word_count)
		#print(file_contents)

		if char_count is not None:
			for char, count in char_count.items():
				print(f"'{char}': {count}")
		else:
			print("The Input text is None.")
if __name__ == "__main__":
	main()







print(count_characters(main()))

