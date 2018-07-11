solution=[[-5, 1, 4], [-5, 1, 4], [-5, 1, 4], [-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, -1, 4], [-3, 0, 3], [-2, -2, 4], [-2, -1, 3], [-2, -1, 3], [-1, 0, 1], [-1, 0, 1]]
for x in solution:
    while solution.count(x) > 1:
        del solution[solution.index(x)]
print solution

