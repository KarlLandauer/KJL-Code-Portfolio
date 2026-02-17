# Let's design a basic multiplication program... just the practice for now

import random

from openai import OpenAI
import os

key = OpenAI(api_key=os.getenv("SECRET_API"))


choice = input(
    'What would you like to do? Multiples/Addition/Subtraction/Division/AI: ').strip().lower()


def ai_question():

    question = input("Please write your question Here: ")

    print('AI is thinking......')
    print('\n')
    answer = key.responses.create(
        model="gpt-5-nano",
        input=question + 'use minimum tokens keep answer short, answer must be understood by a grade 6 - only allowed to answer maths questions - always explain how you got to the answer mathematically',
        store=False
    )

    print(answer.output_text)
    print('\n')

    ask_again = input("Do you want to continue - yes or no? ").strip().lower()
    if ask_again == 'no':
        restart_program()


def restart_program():

    choice = input(
        'What would you like to do? Multiples/Addition/Subtraction/Division/AI: ').strip().lower()

    while True:

        if choice == 'multiples':
            multiplication()

        elif choice == 'addition':
            addition()

        elif choice == 'subtraction':
            subtraction()

        elif choice == 'division':
            division()

        elif choice == 'ai':
            ai_question()

        else:
            print('Please chek your spelling!')
            print("\n")
            choice = input(
                'What would you like to do? Multiples/Addition/Subtraction/Division: ').strip().lower()


def division():

    max_number = 2
    score = 0
    level = 1

    while True:

        print("You are in division mode")

        a = random.randint(1, 9)
        b = random.randint(1, max_number)

        try:

            answer = float(input('What is' + " " + f"{a} / {b}? "))

        except ValueError:
            print('Please enter a number')
            print('Current Level:' + str(level))
            print('Current Score:' + str(score))
            print("\n")

            continue

        if answer == a / b:
            print("Well done!")
            score += 1
            print('level' + ' ' + str(level))

            print('Current Score:' + str(score))

        else:
            print("Wrong answer")
            print()

            print("Please wait, AI is thinking - Response can take up to 90 seconds")

            response = key.responses.create(
                model="gpt-5-nano",
                input=f"{a} / {b} explain to the student how this sum works.  keep explanation short.  It for grade 4 - 8 so keep it simple langauge. Only answer the question",
                store=False
            )

            print(response.output_text)
            print('\n')

        if (score % 10 == 0 and score != 0):
            max_number += 1
            level += 1
            print("New Level")
            print('Current Level:' + str(level))

        if score % 5 == 0 and score != 0:
            restart = input(
                'Do you want to continue - yes or no? ').strip().lower()

            if restart == 'no':
                print('\n')
                restart_program()


def subtraction():

    max_number = 2
    score = 0
    level = 1

    while True:

        print("You are in subtraction mode")

        a = random.randint(1, 9)
        b = random.randint(1, max_number)

        try:

            answer = int(input('What is' + " " + f"{a} - {b}? "))

        except ValueError:
            print('Please enter a number')
            print('Current Level:' + str(level))
            print('Current Score:' + str(score))
            print("\n")

            continue

        if answer == a - b:
            print("Well done!")
            print('\n')
            score += 1
            print('level' + ' ' + str(level))

            print('Current Score:' + str(score))

        else:

            print("Wrong answer")
            print('\n')

            print("Please wait, AI is thinking - Response can take up to 90 seconds")

            response = key.responses.create(
                model="gpt-5-nano",
                input=f"{a} - {b} explain to the student how this sum works.  keep explanation short.  It for grade 4 - 8 so keep it simple langauge. Only answer the question",
                store=False
            )

            print(response.output_text)
            print('\n')

        if (score % 10 == 0 and score != 0):
            max_number += 1
            level += 1
            print("New Level")
            print('Current Level:' + str(level))

        if score % 5 == 0 and score != 0:
            restart = input(
                'Do you want to continue - yes or no? ').strip().lower()

            if restart == 'no':
                print('\n')
                restart_program()


def addition():

    max_number = 2
    score = 0
    level = 1

    while True:

        print("You are in addition mode")

        a = random.randint(1, 9)
        b = random.randint(1, max_number)

        try:

            answer = int(input('What is' + " " + f"{a} + {b}? "))

        except ValueError:
            print('Please enter a number')
            print('Current Level:' + str(level))
            print('Current Score:' + str(score))
            print("\n")

            continue

        if answer == a + b:
            print('\n')
            print("Well done!")
            score += 1
            print('level' + ' ' + str(level))

            print('Current Score:' + str(score))

        else:

            print("Wrong answer")
            print('\n')

            print("Please wait, AI is thinking - Response can take up to 90 seconds")

            response = key.responses.create(
                model="gpt-5-nano",
                input=f"{a} + {b} explain to the student how this sum works.  keep explanation short.  It for grade 4 - 8 so keep it simple langauge. Only answer the question",
                store=False
            )

            print(response.output_text)
            print('\n')

        if (score % 10 == 0 and score != 0):
            max_number += 1
            level += 1
            print("New Level")
            print('Current Level:' + str(level))

        if score % 5 == 0 and score != 0:
            restart = input(
                'Do you want to continue - yes or no? ').strip().lower()

            if restart == 'no':
                print('\n')
                restart_program()


def multiplication():

    max_number = 2
    score = 0
    level = 1

    while True:

        print("You are in multiplication mode")

        a = random.randint(1, 9)
        b = random.randint(1, max_number)

        try:

            answer = int(input('What is' + " " + f"{a} * {b}? "))

        except ValueError:
            print('Please enter a number')
            print('Current Level:' + str(level))
            print('Current Score:' + str(score))
            print("\n")

            continue

        if answer == a * b:
            print("Well done!")
            score += 1
            print('level' + ' ' + str(level))

            print('Current Score:' + str(score))

        else:

            print("Wrong answer")
            print('\n')

            print("Please wait, AI is thinking - Response can take up to 90 seconds")

            response = key.responses.create(
                model="gpt-5-nano",
                input=f"{a} * {b} explain to the student how this sum works.  keep explanation short.  It for grade 4 - 8 so keep it simple langauge. Only answer the question",
                store=False
            )

            print(response.output_text)
            print('\n')

        if (score % 10 == 0 and score != 0):
            max_number += 1
            level += 1
            print("New Level")
            print('Current Level:' + str(level))

        if score % 5 == 0 and score != 0:
            restart = input(
                'Do you want to continue - yes or no? ').strip().lower()

            if restart == 'no':
                print('\n')
                restart_program()


while True:

    if choice == 'multiples':
        multiplication()

    elif choice == 'addition':
        addition()

    elif choice == 'subtraction':
        subtraction()

    elif choice == 'division':
        division()

    elif choice == 'ai':
        ai_question()

    else:
        print('Please chek your spelling!')
        print("\n")
        choice = input(
            'What would you like to do? Multiples/Addition/Subtraction/Division/AI: ').strip().lower()
