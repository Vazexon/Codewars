"""
Function that differentiates a polynomial (a1x^b1+a2x^b2+...+anx^bn)
for a given value of x
"""
import re
def differentiate(polinom, point):
    #a1x^b1+a2x^b2+...+anx^bn
    first_x = polinom.find("x")
    if first_x < 0 or polinom == "":
        return 0
    a = polinom[ :first_x]
    if '+' in a and len(a) == 1:
        a = 1
    min = polinom.find("-")
    if min == 0 and len(a) == 1:
        a = -1
    if first_x == 0:
        a = 1
    a = int(a)
    sign = re.findall("[+-]", polinom[first_x: ])
    if sign == []:
        b = re.findall("[\^?\d*]", polinom[first_x: ])
    else:
        oper = polinom.find(sign[0], first_x, )
        b = re.findall("[\^?\d*]", polinom[first_x: oper])
    if '^' in b:
        b = int(''.join(b[1: ]))
    else:
        b = 1
    if sign == []:
        return a * b  * point ** (b - 1) + differentiate("", point)
    else:
        return a * b  * point ** (b - 1) + differentiate(polinom[oper: ], point)

print(differentiate("x^2", 59884848483559))

"""
or this

from re import finditer

def differentiate(equation, point):
    res = 0

    for exp in finditer(r'([\+\-])?(\d*)?x\^?(\d+)?', equation):
        sign = -1 if exp.group(1) == '-' else 1
        scalar = int(exp.group(2)) if exp.group(2) else 1
        power = int(exp.group(3)) if exp.group(3) else 1

        res += sign * (power * scalar) * point ** (power - 1)

    return res

"""
