
"""Codewars style ranking system"""
class User:
    def __init__(self):
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.progress = 0

    def inc_progress(self, act_rank):
        rank = self.rank
        ranks = self.ranks
        if act_rank not in ranks:
            raise ValueError("Incorrect activity rank!")
        if rank != 8:
            differ = ranks.index(act_rank) - ranks.index(rank)
            if differ > 0:
                self.progress += 10 * differ**2
            elif differ == 0:
                self.progress += 3
            elif differ == -1:
                self.progress += 1
            if self.progress >= 100:
                up_rank = int(str(self.progress)[ :-2])
                self.rank = ranks[ranks.index(rank) + up_rank]
                self.progress -= up_rank * 100
                if self.rank == 8:
                    self.rank = 8
                    self.progress = 0

user = User()
print(user.rank) # => -8
print("******************")
print(user.progress) # => 0
print("******************")
user.inc_progress(-7)
print("******************")
print(user.progress) # => 10
print("******************")
user.inc_progress(-5) # will add 90 progress
print("******************")
print(user.progress) # => 0 # progress is now zero
print("******************")
print(user.rank) # => -7 # rank was upgraded to -7
