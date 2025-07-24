# def grade(score):
#     if score >= 50:
#         print("You passed")
#         if score >= 80:
#             print("Grade A")
#         elif score >= 70:
#             print("Grade B")
#         elif score >= 60:
#             print("Grade C")
#         else:
#             print("Grade D")
#     else:
#         print("You failed")

# score1 = int(input("Student1 score = "))
# grade(score1)
# score2 = int(input("Student2 score = "))
# grade(score2)
# score3 = int(input("Student3 score = "))
# grade(score3)

# num1 = int(input("Num 1: "))
# num2 = int(input("Num 2: "))


def ui_sudcoon(x, z):
     for i in range (1,z+1):
        print(f"{x} x {i} = {x*i}")
  
ui_sudcoon(2, 12)