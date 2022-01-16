from itertools import combinations
def game(p1_hp, p1_dmg, p1_armor, p2_hp, p2_dmg, p2_armor):
    over = False
    while over == False:
        hits = p1_dmg - p2_armor
        if hits <= 0:
            hits = 1
        p2_hp = p2_hp - hits
        if p2_hp <= 0:
            return True
        hits = p2_dmg - p1_armor
        if hits <= 0:
            hits = 1
        p1_hp = p1_hp - hits
        if p1_hp <= 0:
            return False

# cost / damage / armor
weapons = {"dagger": [8, 4, 0], "shortsword": [10, 5, 0], "warhammer": [25, 6, 0], "longsword": [40, 7, 0], "greataxe": [74, 8, 0]};
armors = {"none": [0, 0, 0], "leather": [13, 0, 1], "chainmail": [31, 0, 2], "splintmail": [53, 0, 3], "bandedmail": [75, 0, 4], "platemail": [102, 0, 5]}
rings = {"d1": [25, 1, 0], "d2": [50, 2, 0], "d3": [100, 3, 0], "de1": [20, 0, 1], "de2": [40, 0, 2], "de3": [80, 0, 3]}

most_gold = 0
for w in weapons:
    for a in armors:
        cost = weapons[w][0]
        damage = weapons[w][1]
        armor = weapons[w][2]
        cost = cost + armors[a][0]
        damage = damage + armors[a][1]
        armor = armor + armors[a][2]

        if game(100, damage, armor, 100, 8, 2) == False and cost > most_gold:
            most_gold = cost

        for r in rings:
            new_cost = cost + rings[r][0]
            new_damage = damage + rings[r][1]
            new_armor = armor + rings[r][2]

            if game(100, new_damage, new_armor, 100, 8, 2) == False and new_cost > most_gold:
                most_gold = new_cost
        for r in set(list(combinations(rings, 2))):
            new_cost = cost + rings[r[0]][0]
            new_damage = damage + rings[r[0]][1]
            new_armor = armor + rings[r[0]][2]
            new_cost = new_cost + rings[r[1]][0]
            new_damage = new_damage + rings[r[1]][1]
            new_armor = new_armor + rings[r[1]][2]

            if game(100, new_damage, new_armor, 100, 8, 2) == False and new_cost > most_gold:
                most_gold = new_cost

print(most_gold)