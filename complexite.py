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