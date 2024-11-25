import string
import keyword

invalid_characters = list(string.punctuation)
invalid_characters.remove("_")

str = input("Enter your name:")
if str[0].isdigit():
    print(False)
elif any([c.isupper() for c in str]):
    print(False)
elif any([c in invalid_characters for c in str]):
    print(False)
elif str in keyword.kwlist:
    print(False)
elif any([c == " " for c in str]):
    print(False)
else:
    print(True)

