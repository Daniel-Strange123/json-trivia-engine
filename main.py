import json
import random
score = 0

print("Hello user, what is your name?")
name = input("Enter your name: ")
print(f"Welcome {name} to the ultimate guessing game")
print("Do you wish to indulge me?")
answer = input("Answer only yes or no: ")

while True:
    if answer == "yes":
        with open("questions.json", "r") as file:
            questions_data = json.load(file)
            if len(questions_data) >= 10:
                quiz_questions = random.sample(questions_data,10)
            else:
                quiz_questions = questions_data

            question_number = 1
        for item in quiz_questions:
            print(f"\nQuestion {question_number} of 10:")
            print(f"{item['question']}")
            for index, option in enumerate (item["options"], start =1):
                print(f"{index}.{option}")    
             #get user choice
            user_choice = input("Enter your answer: ")
            correct_answer = item["answer"]
            if user_choice.lower() == correct_answer.lower():
                print("That is correct!!!")
                score += 1
            else:
                print(f"That is incorrect!!, the correct asnwer is {correct_answer}")
    
            question_number += 1
    else:
        print("Goodbye!!")
    break                          
            
print(f"\n Quiz Complete!")
print(f"Your Final Score: {score}/10")


if score == 10:
    print("That is very good, you had a perfect score!!")
elif score < 10:
    print("Hats off for the attempt, there is always next time.")
else:
    print("Poor!!!")
    

               
        

