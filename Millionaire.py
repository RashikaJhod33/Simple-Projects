# MILLIONAIRE GAME USING PYTHON

questions = [["What is the capital of India?", "New delhi", "Bhopal", "Punjab", "Rajisthan", 1],
             ["How many states in India?", 28, 29, 30, 52, 2],
             ["Who is the president of India?", "Rajnath Singh", "Ramnath Kovind", "Draupadi Murmu", "Narendra Modi", 3]]

prizes = [5000,4000,3000]
i= 0
for q in questions:
    print(q[0])
    print(f"a.{q[1]}")
    print(f"b.{q[2]}")
    print(f"c.{q[3]}")
    print(f"d.{q[4]}")

    answer = int(input("Enter your answer: 1 for a,2 for b,3 for c,4 for d :-"))
    if (q[5]==answer):
        print("Your answer is correct.")
    else:
        print(f"Incorrect, Correct answer is {q[5]}.")
        print("Better luck next time.")
        break
    print(f"you won {prizes[i]}")
    i += 1
        

        


    
    
    



