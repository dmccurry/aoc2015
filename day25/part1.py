target_row = 2978
target_col = 3083
current_row = 1
current_col = 1
current_value = 20151125

while current_row != target_row or current_col != target_col:
    next_value = current_value * 252533
    next_value = next_value % 33554393

    if current_row == 1:
        current_row = current_col + 1
        current_col = 1
    else:
        current_row -= 1
        current_col += 1
    current_value = next_value

print(current_value)