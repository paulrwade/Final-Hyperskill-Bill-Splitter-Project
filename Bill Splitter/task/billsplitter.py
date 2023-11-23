import random


print("Enter the number of friends joining (including you):")

number_of_attendees = int(input())
name_of_lucky_person = ""

print("")

if number_of_attendees <= 0:

    print("No one is joining for the party")

else:

    my_dictionary = dict()

    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(number_of_attendees):

        my_dictionary[input()] = 0

    bill_amount = float(input("Enter the total bill value:"))

    perform_who_is_lucky = str(input('Do you want to use the "Who is Lucky?" feature? Write Yes/No:'))

    if perform_who_is_lucky == "Yes":

        number_of_person_selected = int(random.randint(1, number_of_attendees) - 1)

        name_of_lucky_person = list(my_dictionary.keys())[number_of_person_selected]

        print(name_of_lucky_person, "is the lucky one!")

        per_person_amount = round((bill_amount / (number_of_attendees - 1)), 2)

    else:

        print("No one is going to be lucky.")

        per_person_amount = round((bill_amount / number_of_attendees), 2)

    for key in my_dictionary:
        if perform_who_is_lucky == "Yes" and key == name_of_lucky_person:
            my_dictionary[key] = 0.0
        else:
            my_dictionary[key] = per_person_amount

    print("")
    print(my_dictionary)
