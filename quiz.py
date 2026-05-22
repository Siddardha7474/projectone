score = 0
q1 = input("Python is interpreted language? yes/no: ")
if q1.lower() == "yes":
    score += 1
q2 = input("2 + 2 = ")
if q2 == "4":
    score += 1
print("Score:", score)