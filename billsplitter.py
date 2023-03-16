import random

print("Enter the number of friends joining (including you):")
people_count = int(input())
people_list = []

if people_count == 0 or people_count < 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")

for _ in range(people_count):
    name = input()
    people_list.append(name)

people_dict = dict.fromkeys(people_list, 0)

total_bill = float(input("Enter the total bill value:\n"))

lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:').lower()


if lucky == 'yes':
    lucky_person = random.choice(people_list)
    print(f"{lucky_person} is the lucky one!")
    splitted_bill = round(total_bill / (people_count - 1), 2)
    people_dict = {x: splitted_bill for x in people_dict}
    people_dict.update({lucky_person: 0})

else:
    print("No one is going to be lucky")
    splitted_bill = round(total_bill / people_count, 2)
    people_dict = {x: splitted_bill for x in people_dict}

print(people_dict)