#One Method
"""
def censor(text,word):
    edit = text
    l = len(word)
    for i in range(len(text)-len(word)+1):
        j = i + l
        if edit[i:j] == word:
            edit = edit[:i] + "*" * l + edit[j:]
        print edit
    return edit
"""
 #Better Method
def censor(text,word):
    edit = text.split()
    l = len(word)
    for key,i in enumerate(edit):
        if i == word:
            edit[key] = "*" * l
    return " ".join(edit)        


print censor("this hack is wack hack", "hack")          