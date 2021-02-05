def unique_pairs(n):
    """Produce pairs of indexes in range(n)"""
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

s = "a string to examine"
for i, j in unique_pairs(len(s)):
    if s[i] == s[j]:
        answer = (i, j)
        break

print(unique_pairs(s))
