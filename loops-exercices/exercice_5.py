nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [x for x in nombres if x % 2 == 0]
"""
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
"""

print(nombres_pairs)

# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [x for x in nombres if x >= 0]
"""
for i in nombres:
    if i >= 0:
        nombres_positifs.append(i)
"""

print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [x*2 for x in nombres]
"""
for i in nombres:
    nombres_doubles.append(i * 2)
"""

print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [x if x % 2 == 0 else -x for x in nombres]

"""
for i in nombres:
    if i % 2 == 0:
        nombres_inverses.append(i)
    else:
        nombres_inverses.append(-i)
"""

print(nombres_inverses)
