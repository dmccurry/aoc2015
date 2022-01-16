def get_score(ingredients):
    capacity = []
    durability = []
    flavor = []
    texture = []
    calories = []

    for ingredient in ingredients:
        capacity.append(ingredients[ingredient][0] * ingredients[ingredient][5])
        durability.append(ingredients[ingredient][1] * ingredients[ingredient][5])
        flavor.append(ingredients[ingredient][2] * ingredients[ingredient][5])
        texture.append(ingredients[ingredient][3] * ingredients[ingredient][5])
        calories.append(ingredients[ingredient][4] * ingredients[ingredient][5])
    total_capacity = sum(capacity)
    total_durability = sum(durability)
    total_flavor = sum(flavor)
    total_texture = sum(texture)
    total_calories = sum(calories)

    if total_capacity < 0:
        total_capacity = 0
    if total_durability < 0:
        total_durability = 0
    if total_flavor < 0:
        total_flavor = 0
    if total_texture < 0:
        total_texture = 0
    if total_calories != 500:
        return 0

    return total_capacity * total_durability * total_flavor * total_texture

input_file = open("input", "r")
ingredients = {}
ingredient_list = []

for line in input_file:
    parts = line.split(" ")
    ingredient = parts[0]
    capacity = int(parts[2].replace(",", ""))
    durability = int(parts[4].replace(",", ""))
    flavor = int(parts[6].replace(",", ""))
    texture = int(parts[8].replace(",", ""))
    calories = int(parts[10])

    ingredient_list.append(ingredient)
    ingredients[ingredient] = [capacity, durability, flavor, texture, calories, 0]

max_score = 0
for i in range(0, 100):
    for j in range(0, 100):
        for k in range(0, 100):
            ingredients[ingredient_list[0]][5] = i
            ingredients[ingredient_list[1]][5] = j
            ingredients[ingredient_list[2]][5] = k
            ingredients[ingredient_list[3]][5] = 100 - i - j - k

            score = get_score(ingredients)
            if score > max_score:
                max_score = score
print(max_score)

