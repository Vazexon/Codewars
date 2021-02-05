"""
Given the count of each of the races on the side of good, followed by the count
of each of the races on the side of evil, determine which side wins
"""

import re
def goodVsEvil(good, evil):
    gud = re.findall(r"\d+", good)
    ewheel = re.findall(r"\d+", evil)
    gg = [ int(g) for g in gud ]
    eg = [ int(e) for e in ewheel ]
    s_good = gg[0] + gg[1] * 2 + gg[2] * 3 + gg[3] *3 + gg[4] * 4 + gg[5] * 10
    s_evil = eg[0] + eg[1] * 2 + eg[2] * 2 + eg[3] *2 + eg[4] * 3 + eg[5] * 5 + eg[6] * 10
    if s_good > s_evil:
        return 'Battle Result: Good triumphs over Evil'
    elif s_good < s_evil:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
