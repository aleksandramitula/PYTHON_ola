old = list(range(10))
new = old[:]
# old and new = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for indeks, wart in enumerate(old):
    print(f"{indeks} : {wart} ")
    new[indeks] = wart ** 2

print(old)
print(new)