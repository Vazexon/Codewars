"""
Returns a list of possible triplets with the specified sum
"""
    
def sum_of_3_0(our_list, our_sum):
    result = []
    n = len(our_list)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                triplet = sorted([our_list[i], our_list[j], our_list[k]])
                if sum(triplet) == our_sum and triplet not in result:
                    result.append(triplet)
    print(f"List of possible triplets: {result}.")

with open("array.txt", 'r') as f:
    data = f.read()
    res = [int(i) for i in data.split()]

sum_of_3_0(res, 0)
