# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


text = input("String of text: ")
vogais = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for c in vogais:
    if c in text:
        text = text.replace(c, "")
print(text)