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
            
        
            categories = set()
            for q in questions_data:
                categories.add(q["category"])
            for cat in categories:
                print("-", cat)    

          
            choice = input("Enter a category: ")
            while choice not in categories:
                choice = input("Enter a valid category: ")
            filtered = []
            
            for q in questions_data:
                if q["category"] == choice:
                    filtered.append (q) 

        
            question_number =1      
            for q in filtered:
                print(f"\nQuestion {question_number} of 10:")
                print("\n", q["question"])
                
               
                for index, option in enumerate (q["options"],start=1) :
                    print(f"{index}.{option}") 
                question_number += 1      
                #get user choice
                user_choice = input("Enter your answer: ")
                correct_answer = q["answer"] 
                if user_choice.lower() == correct_answer.lower():
                    print("That is correct!!!")
                    score += 1
                else: 
                    print(f"That is incorrect!!, ")
                    print(f"The correct answers are {correct_answer}")
            

                if question_number == 11:
                    break
    else:
        print("Goodbye!!")
    break                          
            
print(f"\n Quiz Complete!")

print(f"Your Final Score: {score}/10")


if score == 10:
    print("That is very good, you had a perfect score!!")
else :
    print("Hats off for the attempt, there is always next time.")

    

               
        


























                    

            
       