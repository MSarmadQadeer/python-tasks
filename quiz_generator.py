import random
print("...You Are Going To Attempt The Quiz...\n")
name = input("Dear User Enter Your Name: ").upper()
print("\nDear "+name+"...! HERE THE QUIZ BEGINS.\n")
# 'n' IS FOR QUESTION NUMBER
n = 1
correct = 0
attempt = 0
user_decision = "y"
while user_decision == "y":
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    operator = random.randint(0, 3)
    print("Question No # ", n)
    while operator == 0:
        print(num_1, " + ", num_2, "= ", end="")
        user_input = input()
        if user_input.lstrip("-,+").replace(".", "").isdigit():
            user_answer = eval(user_input)
            answer = num_1+num_2
            if user_answer == answer:
                print("CORRECT ANSWER")
                correct = correct+1
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
            else:
                print("WRONG ANSWER")
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
        else:
            print("Enter A Valid Input")
            continue
        break
    while operator == 1:
        print(num_1, " - ", num_2, "= ", end="")
        user_input = input()
        if user_input.lstrip("-,+".replace(".", "")).isdigit():
            user_answer = eval(user_input)
            answer = num_1-num_2
            if user_answer == answer:
                print("CORRECT ANSWER")
                correct = correct+1
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
            else:
                print("WRONG ANSWER")
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
        else:
            print("Enter A Valid Input")
            continue
        break
    while operator == 2:
        print(num_1, " x ", num_2, "= ", end="")
        user_input = input()
        if user_input.lstrip("-,+").replace(".", "").isdigit():
            user_answer = eval(user_input)
            answer = num_1*num_2
            if user_answer == answer:
                print("CORRECT ANSWER")
                correct = correct+1
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
            else:
                print("WRONG ANSWER")
                attempt = attempt+1
                user_decision = input(
                    "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
        else:
            print("Enter A Valid Input")
            continue
        break
    while operator == 3:
        if num_2 == 0:
            print(num_2, " / ", num_1, "= ", end="")
            user_input = input()
            if user_input.lstrip("-,+").replace(".", "").isdigit():
                user_answer = eval(user_input)
                answer = num_2/num_1
                if user_answer == answer:
                    print("CORRECT ANSWER")
                    correct = correct+1
                    attempt = attempt+1
                    user_decision = input(
                        "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
                else:
                    print("WRONG ANSWER")
                    attempt = attempt+1
                    user_decision = input(
                        "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
            else:
                print("Enter A Valid Input")
                continue
        else:
            print(num_1, " / ", num_2, "= ", end="")
            user_input = input()
            if user_input.lstrip("-,+").replace(".", "").isdigit():
                user_answer = round(eval(user_input), 2)
                answer = round(num_1/num_2, 2)
                if user_answer == answer:
                    print("CORRECT ANSWER")
                    correct = correct+1
                    attempt = attempt+1
                    user_decision = input(
                        "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
                else:
                    print("WRONG ANSWER")
                    attempt = attempt+1
                    user_decision = input(
                        "PRESS 'Y' TO PROCEED AND ANY OTHER KEY TO END: ").lower()
            else:
                print("Enter A Valid Input")
                continue
        break
# HERE IT INCREMENTS THE QUESTION NUMBER
    n = n+1
    print("\n")
print("\n")
print(name + " Your Score Is ", correct, "/", attempt)
