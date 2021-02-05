"""
Strips all text that follows any of a set of comment markers passed in.
"""
def solution(string, markers):
    res = []
    i = 0
    for line in string.split('\n'):
        for m in markers:
            if m in line:
                if len(res) == i + 1 and len(line.split(m)[0].strip()) < len(res[i]) :
                    res.pop()
                res.append(line.split(m)[0].strip())
        if not any(mark in line for mark in markers):
            res.append(line.strip())
        if any(mark in res[-1] for mark in markers):
            res.pop()
        i += 1
    result = "\n".join(res)
    return result

"""
or this

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        res = [v.split(s)[0].strip() for v in parts]
    return '\n'.join(res)
"""
print(solution('lemons pears bananas lemons\n- = # apples ^ #\ncherries\nstrawberries ? oranges', ['@', '^', "'", '-', '=', '.', ',']))
