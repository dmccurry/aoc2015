def is_valid(s):
    if s.count("i") != 0 or s.count("o") !=0 or s.count("l") !=0:
        return False

    n_doubles = 0
    used_doubles = []
    doubles = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "jj", "kk", "mm", "nn", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz"]

    for double in doubles:
        if s.count(double) > 0:
            n_doubles = n_doubles + 1
    
    if n_doubles < 2:
        return False
    
    groups = ["abc", "bcd", "cde", "def", "efg", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]

    for group in groups:
        if s.count(group) > 0:
            return True

    return False

def increment(s):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    parts = list(s)
    for i in range(len(parts) - 1, -1, -1):
        letter = parts[i]
        letter_i = letters.index(letter)
        if letter_i + 1 < len(letters):
            parts[i] = letters[letter_i+1]
            break
        else:
            parts[i] = "a"
    return ''.join(parts)


start = "cqjxxyzz"
next_pass = increment(start)
while is_valid(next_pass) == False:
    next_pass = increment(next_pass)

print(next_pass)