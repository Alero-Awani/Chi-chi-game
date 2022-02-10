import random
from game_data import data 
# from replit import clear

#create a function that creates people 
def person():
  random_index = random.randint(0, 49)
  individual = data[random_index]

  name = individual["name"]
  followers = individual["follower_count"]
  description = individual["description"]
  country = individual["country"]

  return name, followers, description, country



def compare(followers_a, followers_b):
  if followers_a > followers_b:
    higher_followers = followers_a
  else:
    higher_followers = followers_b
  return higher_followers



def check_answer(answer, correct_answer):
  if answer == correct_answer:
    # clear()
    return True
    
  else:
    return



def game():

  print(" ")
  first_person = person()
  second_person = person()

  
  should_continue = True
  score = 0
  while should_continue:
    print(f"Compare A: {first_person[0]}, {first_person[2]} from {first_person[3]} ")
    print(f"Against B: {second_person[0]}, {second_person[2]} from {second_person[3]}")

    answer = input("Who has more followers,Type A or B: ").lower()

    if answer == "a":
      answer = first_person[1]
    else:
      answer = second_person[1]


    higher_followers = compare(first_person[1], second_person[1])

   

    if check_answer(answer, higher_followers):
      score += 1
      print(f"You're right, your current score is {score}")
      first_person = second_person
      second_person = person()
    else:
      print("That was incorrect, Game Over!")
      should_continue = False




 
  
game()
