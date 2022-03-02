# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
life = 42
golden = 1.61
user = "steven averlant"
morning = True
access = None

print(life)
print(golden)
print(user)
print(morning)
print(access)

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez les valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
intg = 2
intg = float(intg)
print(intg)
floating = 1.62
floating = round(floating, 0)
floating = int(floating)
print(floating)