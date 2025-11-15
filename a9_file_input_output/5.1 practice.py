'''read the text from the given file : "5.1.1 practice.txt" and
 search if the word "twinkle" comes in the file'''

with open("5.1.1 poem.txt","r") as f:
  word=input("ehter the word you want to search in the paragraph: ").lower()
  line=f.read().lower
  if(word in line):
    print(f"this paragraph contain the word \"{word}\"")
  else:
    print(f"this paragraph do not contain the word \"{word}\"")
  