import math

# proměnné a řetežce
jmeo= "Petr"
vek = 15
print(f"Jmenuji se {jmeo} a je mi {vek} let.")

numbers = [1,2,3,4,5]

numbers.append(6)
numbers.sort()
print(f"Seřaženy seznam: {numbers}")
print(f" První prevek seznam: {numbers[0]}")
print(f" Poslední prvek seznam: {numbers[-1]}")

data = [3,3,3,4,5,6,7,8,9,9,9,10]
unique_data = set(data)
print(f"Uníkatní hodnoty: {unique_data} ")

for i in range (1, 11):
    if i % 3 == 0:
        print("je dělitelné 3")
    elif i % 5 ==0:
        print("je dělitelné 5")
    else:
        print(i)

def vypocet_obvdu_obdelniku(delka, sirka = 10):
    if sirka is None:
      sirka = delka
    return 2 * (delka + sirka)
delka = 5
sirka = 3

print(f"Obvod obdelniku s dlekou {delka} a sirku {sirka} je : {vypocet_obvdu_obdelniku}")