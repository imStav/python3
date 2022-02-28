#exo 3.1
year = 2022
birthyear = 1988

age = year - birthyear
identity = "Alice"

print("exo 3.1 :")
print(identity, "a", age, "ans")
print()


#exo 3.2
candies = 15
chocolates = 17
friends = 3

candies_rest = candies / 4
chocolates_rest = chocolates / 4

result = round(candies_rest + chocolates_rest)

print("exo 3.2 :")
print("Il reste", result, "bonbons et chocolats à Bob")
print()


#exo 3.3
candies_per_person = candies / 4
chocolates_per_person = chocolates / 4

candies_result = round(candies_per_person)
chocolates_result = round(chocolates_per_person)

bonbons_result = candies_result + chocolates_result
txt = "Bob va distribuer au total"

print("exo 3.3 :")
print(txt, bonbons_result, "bonbons et chocolats par personne")
print()


#exo 3.4
fibo = 1 + 1 + 2 + 3 + 5 + 8 + 13
moyenne = fibo / 7

print("exo 3.4 :")
print("La moyenne est de", moyenne)
print()


#exo 3.5
day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.7
day5 = 32

days = 5

total = day1 + day2 + day3 + day4 + day5
average = round(total / days, 2)

print("exo 3.5 :")
print("Sur", days, "jours")
print("Alice a depensé un total de", total, "euros")
print("Soit, en moyenne,", average, "euros par jour")


#exo 3.6
