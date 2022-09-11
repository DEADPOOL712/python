##################
## Odd v/s Even ##
##################
# number = int(input("Enter number : "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


####################
## else if leader ##
####################
# age = int(input("Enter your age : "))
# if age < 18:
# print("You are under 18 !")
# elif age > 18:
# print("You are abov 18 !")
# else:
# print("You are 18 !")


##################
## Match_OR_not ##
##################
# boy = input("Enter your name :").upper()
# girl = input("Enter their name :").upper()
# T = girl.count("T") + girl.count("R") + girl.count("U") + girl.count(
#     "E") + boy.count("T") + boy.count("R") + boy.count("U") + boy.count("E")
# L = girl.count("L") + girl.count("O") + girl.count("V") + girl.count(
#     "E") + boy.count("L") + boy.count("O") + boy.count("V") + boy.count("E")
# # print(str(T) + str(L))
# total = str(T) + str(L)
# total = int(total)
# if total <= 10 or total >= 90:
#     print("Your score is " + str(total) + "! Sorry ")
# elif total >= 40 and total <= 65:
#     print("You have perfect match !🤩")
# else:
#     print("Sorry you have to try with someone else !")


####################
## Random moodule ##
####################
# random_int = random.randint(1, 10) (including both limits)
# print(random_int)
# random_float = random.random()  # 0.0 to 0.99
# print(random_float * 5)


###################
## Heads / Tails ##
###################
# random_num = random.randint(0, 1)
# if random_num == 1:
#     print("Heads")
# else:
#     print("Tails")


##########
## List ##
##########
# animes = ["narto", "onepiece", "blackclover"]
# print(animes[1])
# print(animes)
# animes.append("jjk")
# print(animes)
# animes.extend(["dragonball", "onepunch man"])
# print(animes)


#####################
## RandomName task ##
#####################
# names = input("Enter name of peoples seperated by '' : ")
# names_list = names.split(",")
# random_name = names_list[random.randint(0, len(names_list)-1)]
# print(f"{random_name} is going to pay the bill !")

# above code can be replace by choice()
# random_name = random.choice(names_list)
# print(f"{random_name} is going to pay the bill !")


###################
## Change Matrix ##
###################
# row1 = ["🟩", "🟩", "🟩"]
# row2 = ["🟩", "🟩", "🟩"]
# row3 = ["🟩", "🟩", "🟩"]
# matrix = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# pos = int(input("Enter place to change (row,colunm) : "))
# index_row = int(pos/10)
# index_clm = pos % 10
# matrix[index_row-1][index_clm-1] = "⭕"
# print(f"{row1}\n{row2}\n{row3}")


#########################
## Rock/Paper/Scissors ##
#########################
# ASCII art save into variable
# Rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# Paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# Scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# combined = [Rock, Paper, Scissors]
# user = int(input("Enter 0 for rock 1 for paper and 2 for scissors : "))
# computer = random.randint(0, 2)
# if (computer == 0 and user == 1) or (computer == 1 and user == 2) or (computer == 2 and user == 0):
#     print("\n   ****** You win ! ******   \n")
#     print(f"computer : \n{combined[computer]}")
#     print(f"User : \n{combined[user]}")
# elif (computer == 0 and user == 2) or (computer == 1 and user == 0) or (computer == 2 and user == 1):
#     print("\n   ****** computer win ! ******   \n")
#     print(f"computer : \n{combined[computer]}")
#     print(f"User : \n{combined[user]}")
# else:
#     print("\n   ****** Draw ! ******   \n")
#     print(f"computer : \n{combined[computer]}")
#     print(f"User : \n{combined[user]}")


############
## Loop's ##
############
# animes = ["Naruto", "HQ holder", "spyfamily"]
# for anime in animes:
#     print(anime)
#     print(anime + " Wactched !")


#############
## average ##
#############
# numbers = input("Enter numbers for avg : ").split(" ")
# for i in range(0, len(numbers)):
#     numbers[i] = int(numbers[i])
# total = 0
# for j in numbers:
#     total += j
# print(total/len(numbers))


#############
## Max_Num ##
#############
# scores = input("Enter scores : ").split(" ")
# for i in range(0, len(scores)):
#     scores[i] = int(scores[i])
# print(scores)
# maxScore = 0
# for i in scores:
#     if i > maxScore:
#         maxScore = i
# print(f"The max score above all is {maxScore}")


#################
## Sum_of_even ##
#################
# sumEven = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sumEven += i
# print(sumEven)


#######################
## FizzBuzz Queation ##
#######################
# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


##########################
## Password generator ! ##
##########################
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# combied = []
# for i in range(0, nr_numbers):
#     combied.append(random.choice(numbers))
# for i in range(0, nr_symbols):
#     combied.append(random.choice(symbols))
# for i in range(0, nr_letters-(nr_symbols+nr_numbers)):
#     combied.append(random.choice(letters))
# random.shuffle(combied)
# pas = ""
# for char in combied:
#     pas += char
# print(f"Your generated password : {pas}")


########################
## Task encode/decode ##
########################
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#             'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Exite = False
# # >>> function definition
# def caesar(text_par, shift_par, direction_par):
#     message = ""
#     if direction_par == "encode":
#         for char in text_par:
#             if not char in alphabet:  #>>> to check number/symbole/alphabet
#                 if char == " ":
#                     message += " "
#                 else:
#                     message += "*"
#             else:
#                 letter = alphabet[alphabet.index(char)+shift_par]
#                 message += letter
#         print(f'The encrypted msg is 🎭 " {message} "')
#     elif direction_par == "decode":
#         for char in text_par:
#             if not char in alphabet:  #>>> to check number/symbole/alphabet
#                 if char == " ":
#                     message += " "
#                 else:
#                     message += "*"
#             else:
#                 letter = alphabet[alphabet.index(char)-shift_par]
#                 message += letter
#         print(f'The dcodeed msg is 🎭 " {message} "')
#     else:
#         print("Not valid input ! 🚫")

# # >>> function calling until exite
# while (not Exite):
#     direction = input(
#         "Type 'encode' to encrypt 🔒 , type 'decode' to decrypt 🔓 :\n")
#     text = input("Type your message 📝:\n").lower()
#     shift = int(input("Type the shift number ⏩ :\n"))
#     shift = shift % 29 #>>> to get shift number in range of list
#     caesar(text, shift, direction)
#     check = input("\nYou want to continue enter yes/no  !\n") #>>> to exit loop
#     if check == "yes":
#         Exite = False
#     else:
#         print("Good bye :D ")
#         Exite = True


#######################
## Python dictionary ##
#######################
# programing_dictionary = {
#     "bug": "An erro while running ",
#     "program": "set of instructions given to computer "
# }
# print(programing_dictionary["bug"])
# programing_dictionary["new"] = "To add new element in dictionary"
# print(programing_dictionary)

# for key in programing_dictionary:
#     print(key)
#     print(programing_dictionary[key])


########################
## Task of dictionary ##
########################
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades = {}
# marks = 0
# for key in student_scores:
#     marks = student_scores[key]
#     if marks >= 91 and marks <= 100:
#         student_grades[key] = "outstanding marks !"
#     elif marks >= 81 and marks <= 90:
#         student_grades[key] = "good marks !"
#     else:
#         student_grades[key] = "work hard !"
# print(student_grades)


##############
## Neesting ##
##############
# statedictionary = {
#     "gujrat": {
#         "capital": "gandhinager",
#         "smcity": "surat"
#     },
#     "Goa": {
#         "capital": "goa",
#         "smcity": "pune"
#     }
# }
# print(statedictionary)
# statelist = [{"gujrat": {"capital": "gandhinager",
#                          "smcity": "surat"}}, "ele1", ["c", "d"]]
# print(statelist[0])
# print("Tast")
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]


# def add_new_country(main_par, visits_par, list_par):
#     creat = {
#         "country": main_par,
#         "visis": visits_par,
#         "cities": list_par
#     }
#     travel_log.append(creat)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


####################
## blind-bid task ##
####################
# import os
# all_biders = []
# Exit = False
# other = ""
# higher = 0
# winner = ""
# # function to add biders

# def add_to_list(name_par, bidamount_par):
#     all_biders.append({
#         "name": name_par,
#         "bidamount": bidamount_par
#     })

# # to add name and bidamount
# while (not Exit):
#     name = input("Enter you name ? : ")
#     bidamount = int(input("Enter bid amount 💵 : "))
#     add_to_list(name, bidamount)
#     other = input("Are there any other biders yes/no ! \n ")
#     if other == "no":
#         Exit = True
#     else:
#         os.system('cls')

# # to check winner
# for dictionary in all_biders:
#     if dictionary["bidamount"] > higher:
#         higher = dictionary["bidamount"]
#         winner = dictionary["name"]
# print(f"\nThe winner is {winner} with amount of {higher} 💵")


###################################
## Function with return , task ! ##
###################################
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return "Leap year."
#             else:
#                 return "Not leap year."
#         else:
#             return "Leap year."
#     else:
#         return "Not leap year."

# def days_in_month(year_par, month_par):
#     """Take the year and month and give days in it """
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year_par) == "Leap year." and month_par == 2:
#         return 29
#     return month_days[month_par-1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


###################
## calculator🪲 ##
##################
# functions for calculation
# # bug : try to exit program after one time run gain (0 -- than X --)

# def add(num1, num2):
#     return num1+num2

# def sub(num1, num2):
#     return num1-num2

# def multi(num1, num2):
#     return num1*num2

# def div(num1, num2):
#     return num1/num2

# # dictionary that hold all calulation
# calulation = {
#     "+": add,
#     "-": sub,
#     "*": multi,
#     "/": div,
# }
# # for callin function and taking input from user
# def cal():
#     Exite = False
#     num1 = float(input("Enter first number :"))
#     for sym in calulation:
#         print(sym)
#     while (not Exite):
#         sym = input("Enter operator for calculation :")
#         num2 = float(input("Enter second number :"))
#         new_fun = calulation[sym]
#         print(f"{num1}{sym}{num2} = {new_fun(num1, num2)}")
#         again = input(
#             f"Enter 'y' to containue calcultion  with {new_fun(num1, num2)}and '0' to start again 'x' to exit program : ")
#         if again == 'y':
#             num1 = new_fun(num1, num2)
#         else:
#             os.system('cls')
#             if again == 'x':
#                 Exite = True
#             else:
#                 cal()
# cal()


####################
## BlackJack Game ##
####################
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score > 21 and computer_score > 21:
#         return "You went over. You lose 😤"

#     if user_score == computer_score:
#         return "Draw 🙃"
#     elif computer_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif user_score == 0:
#         return "Win with a Blackjack 😎"
#     elif user_score > 21:
#         return "You went over. You lose 😭"
#     elif computer_score > 21:
#         return "Opponent went over. You win 😁"
#     elif user_score > computer_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"

# def play_game():

#     user_cards = []
#     computer_cards = []
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"   Your cards: {user_cards}, current score: {user_score}")
#         print(f"   Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input(
#                 "Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"   Your final hand: {user_cards}, final score: {user_score}")
#     print(
#         f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     play_game()


##################
## guess number ##
##################
# import random
# random_num = random.randint(1, 100)
# is_over = False
# guessd = 0
# life = 10
# level = input("'easy or 'hard : ")
# if level == 'hard':
#     life = 5
# print(random_num)
# while (not is_over):
#     print(f"you have lives left : {life} ")
#     guessd = int(input("Guess number 1 <num< 100 : "))
#     if guessd == random_num:
#         print("Correct guess !")
#         is_over = True
#     elif guessd > random_num:
#         life -= 1
#         print("high !")
#     elif guessd < random_num:
#         print("low")
#         life -= 1
#     if life == 0:
#         is_over = True
#         print("Sorry you lost all lives")


#####################
## Higher or Lower ##
#####################
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#         'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]

# # select random from dictionary
# account_a = ""
# account_b = ""
# check_return = True
# Final_score = 0

# def random_data():
#     """random selection from data"""
#     return random.choice(data)

# def check_answer(guess, a, b):
#     if a > b:
#         return guess == 'a'
#     else:
#         return guess == 'b'


# account_a = random_data()
# account_b = random_data()
# while account_a == account_b:
#     account_b = random_data()

# while check_return:
#     print(
#         f"\nA : {account_a['name']} is {account_a['description']} from {account_a['country']}")
#     print(
#         f"B : {account_b['name']} is {account_b['description']} from {account_b['country']} \n")
#     user_guess = input('Enter "a" or "b which one has highest followers : ')
#     check_return = check_answer(
#         user_guess, account_a["follower_count"], account_b["follower_count"])
#     if check_return:
#         os.system('cls')
#         Final_score += 1
#         if account_a['follower_count'] > account_b['follower_count']:
#             account_b = random_data()
#         else:
#             account_a = account_b
#             account_b = random_data()
#     else:
#         os.system('cls')
#         print("Wrong answer !")
#         print(f"Your final socre is : {Final_score}")
