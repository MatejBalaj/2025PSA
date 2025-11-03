def vyhod_medzery(text):
     retazec = ""
     for c in text:
         if c!=" ":
             retazec += c
     return retazec

def vyhod_medzery2(text):
    return text.replace(" ", "")

print(vyhod_medzery2("A B C D E F G H"))
print(vyhod_medzery2("a     b     c             c   d"))