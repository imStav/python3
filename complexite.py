#efficacité (ou complexité) :
# - temps d'exécution
# - espace mémoire

# notation de Landau : O() //lettre O, pas le chiffre 0
# n'est pas une fonction, mais un ensemble

# O(c) //c = constante
# O(1)
result = 123 + 42
print(result)


# O(n)
# n, est la quantité de données à traiter
numbers = [123, 42, 3.14]

for number in numbers:
    result = number * 2
    print(result)


# O(n * n) = O(n ** 2)
# n, est la quantité de données à traiter de la première liste
# n, est la quantité de données à traiter de la deuxième liste
numbers = [123, 42, 3.14]
more_numbers = [2.71, 3.14, 0, 53]
common_numbers = []

for number in numbers:
    for more_number in more_numbers:
        if number == more_number:
            common_numbers.append(number)


# O(n * n) = O(n ** 2)
matrix = [
    [123, 42, 3.14],
    [2.71, 3.14, 0],
    [1, 2, 3]
]

for line in matrix:
    for number in line:
        result = number * 2
        print(result)


# O( n * n * n) = O(n3)
cube = [
    [
        ['a1', 'a2', 'a3'],
        ['a4', 'a5', 'a6'],
        ['a7', 'a8', 'a9'],
    ],

    [
        ['b1', 'b2', 'b3'],
        ['b4', 'b5', 'b6'],
        ['b7', 'b8', 'b9'],
    ],

    [
        ['c1', 'c2', 'c3'],
        ['c4', 'c5', 'c6'],
        ['c7', 'c8', 'c9'],
    ]
]

for square in cube:
    for line in square:
        for spot in line:
            print(spot)