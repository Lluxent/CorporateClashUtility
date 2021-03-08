# a meme 'calculated' list of all possible drop permutations, including duplicates
# lol

import math

drops = {
    'Flower Pot'    :   12,
    'Sandbag'       :   20,
    'Bowling Ball'  :   35,
    'Anvil'         :   55,
    'Big Weight'    :   80,
    'Safe'          :   125,
    'Boulder'       :   180,
    'Piano'         :   220
}
comboDamage = [1.0, 1.3, 1.4, 1.5]
PRESTIGE_BONUS = 0.05

output = []

# Two Toon Combos (2 unpres)
for one in drops:
    for two in drops:
        output.append([one, two, math.ceil((drops[one] + drops[two]) * comboDamage[1])])

# Two Toon Combos (1 unpres, 1 pres)
for one in drops:
    for two in drops:
        output.append([one + '*', two, math.ceil((drops[one] + drops[two]) * (comboDamage[1] + (PRESTIGE_BONUS * 1)))])

# Two Toon Combos (2 pres)
for one in drops:
    for two in drops:
        output.append([one + '*', two + '*', math.ceil((drops[one] + drops[two]) * (comboDamage[1] + (PRESTIGE_BONUS * 2)))])

# Three Toon Combos (3 unpres)
for one in drops:
    for two in drops:
        for three in drops:
            output.append([one, two, three, math.ceil((drops[one] + drops[two] + drops[three]) * (comboDamage[2] + (PRESTIGE_BONUS * 0)))])

# Three Toon Combos (2 unpres, 1 pres)
for one in drops:
    for two in drops:
        for three in drops:
            output.append([one + '*', two, three, math.ceil((drops[one] + drops[two] + drops[three]) * (comboDamage[2] + (PRESTIGE_BONUS * 1)))])

# Three Toon Combos (1 unpres, 2 pres)
for one in drops:
    for two in drops:
        for three in drops:
            output.append([one + '*', two + '*', three, math.ceil((drops[one] + drops[two] + drops[three]) * (comboDamage[2] + (PRESTIGE_BONUS * 2)))])

# Three Toon Combos (3 pres)
for one in drops:
    for two in drops:
        for three in drops:
            output.append([one + '*', two + '*', three + '*', math.ceil((drops[one] + drops[two] + drops[three]) * (comboDamage[2] + (PRESTIGE_BONUS * 3)))])            

# Four Toon Combos (4 unpres)
for one in drops:
    for two in drops:
        for three in drops:
            for four in drops:
                output.append([one, two, three, four, math.ceil((drops[one] + drops[two] + drops[three] + drops[four]) * (comboDamage[3] + (PRESTIGE_BONUS * 0)))])

# Four Toon Combos (3 unpres, 1 pres)
for one in drops:
    for two in drops:
        for three in drops:
            for four in drops:
                output.append([one + '*', two, three, four, math.ceil((drops[one] + drops[two] + drops[three] + drops[four]) * (comboDamage[3] + (PRESTIGE_BONUS * 1)))])

# Four Toon Combos (2 unpres, 2 pres)
for one in drops:
    for two in drops:
        for three in drops:
            for four in drops:
                output.append([one + '*', two + '*', three, four, math.ceil((drops[one] + drops[two] + drops[three] + drops[four]) * (comboDamage[3] + (PRESTIGE_BONUS * 2)))])

# Four Toon Combos (1 unpres, 3 pres)
for one in drops:
    for two in drops:
        for three in drops:
            for four in drops:
                output.append([one + '*', two + '*', three + '*', four, math.ceil((drops[one] + drops[two] + drops[three] + drops[four]) * (comboDamage[3] + (PRESTIGE_BONUS * 3)))])

# Four Toon Combos (4 pres)
for one in drops:
    for two in drops:
        for three in drops:
            for four in drops:
                output.append([one + '*', two + '*', three + '*', four + '*', math.ceil((drops[one] + drops[two] + drops[three] + drops[four]) * (comboDamage[3] + (PRESTIGE_BONUS * 4)))])

def final(element):
    return element[-1]

output.sort(key=final)

for entry in output:
    print(entry)