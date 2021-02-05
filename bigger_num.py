from itertools import permutations
def next_bigger(numb):
    numb = str(numb)
    n = len(numb)
    if n < 2:
        return -1
    try:
        for i in reversed(range(n)):
            if numb[i] > numb[i-1]:
                chest = [''.join(p) for p in permutations(numb[i-1: ])]
                chest = sorted([int(c) for c in set(chest)])
                index = chest.index(int(numb[i-1: ]))
                print(chest)
                return int(numb[ :i-1] + str(chest[index + 1]))
        if chest == None:
            return -1
    except:
        return -1

print(next_bigger(80318511))
print(next_bigger(144))
print(next_bigger(414))
print(next_bigger(333))
