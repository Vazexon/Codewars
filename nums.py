from itertools import combinations

result = []

def sum_of_3_0(our_list, our_sum):
   for comb in combinations(our_list, 3):
      triplet = sorted(comb)
      if sum(comb) == our_sum and triplet not in result:
          result.append(triplet)
   print(f"List of possible triplets: {result}.")

with open("array.txt", 'r') as f:
   data = f.read()
   res = [int(i) for i in data.split()]
sum_of_3_0(res, 0)
