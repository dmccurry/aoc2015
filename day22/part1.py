from sys import maxsize
from copy import deepcopy
leastMana = maxsize

def game(p1hp, p1mana, p2hp, cost, activeSpells, turn):
    newActiveSpells = []
    p1armor = 0
    p2dmg = 10
    for i in range(len(activeSpells)):
        if activeSpells[i][3] >= 0:
            p1armor = p1armor + activeSpells[i][4]
            p1mana = p1mana + activeSpells[i][5]
            p2hp = p2hp - activeSpells[i][1]
            p1hp = p1hp + activeSpells[i][2]
        
        newActiveSpell = (activeSpells[i][0], activeSpells[i][1], activeSpells[i][2], activeSpells[i][3] - 1, activeSpells[i][4], activeSpells[i][5], activeSpells[i][6])
        if (newActiveSpell[3] > 0):
            newActiveSpells.append(newActiveSpell)

    if p2hp <= 0:
        global leastMana
        if cost < leastMana:
            leastMana = cost
        return True
    
    if cost >= leastMana:
        return False
    
    if turn == True:
        for spell in spells:
            isActive = False
            for j in range(len(newActiveSpells)):
                if spells[spell][6] == newActiveSpells[j][6]:
                    isActive = True
                    break
            spellCost = spells[spell][0]
            if spellCost <= p1mana and isActive == False:
                a = deepcopy(newActiveSpells)
                a.append(spells[spell])
                game(p1hp, p1mana - spellCost, p2hp, cost + spellCost, a, False)
    else:
        totaldmg = p2dmg - p1armor
        if totaldmg <= 0:
            totaldmg = 1
        p1hp = p1hp - totaldmg
        if p1hp > 0:
            game(p1hp, p1mana, p2hp, cost, newActiveSpells, True)

# cost / damage / hp / turns / armor  / mana / index
spells = {"missile": [53, 4, 0, 0, 0, 0, 0], "drain": [73, 2, 2, 0, 0, 0, 1], "shield": [113, 0, 0, 6, 7, 0, 2], "poison": [173, 3, 0, 6, 0, 0, 3], "recharge": [229, 0, 0, 5, 0, 101, 4]}
p1hp = 50
p1mana = 500
p2hp = 71

activeSpells = []
cost = 0

game(p1hp, p1mana, p2hp, cost, [], True)
print(leastMana)