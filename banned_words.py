"""
Replaces all instances of "you" or "u" (not case sensitive) with "your sister".
"""
import re
def autocorrect(input):
    lst = []
    res_you = re.findall(r"you+[?.:;!]?", input.lower())
    res_u = re.findall(r"u[?.:;!]?", input.lower())
    for word in input.split():
        if word.lower() in res_you or word.lower() in res_u:
            if "!" in word.lower():
                lst.append("your sister!")
            elif "?" in word.lower():
                lst.append("your sister?")
            else:
                lst.append("your sister")
        else:
            lst.append(word)
    result = " ".join(lst)
    return result

autocorrect("I miss you!")
