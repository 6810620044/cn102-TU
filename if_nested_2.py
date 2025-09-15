#
# FILE: if_nested_2.py
# TASK: lab_06
# LANG: PYTHON
# ID:   6810620044
#

#
# Create nested if-else statements.
#

# initial values
score = 0
grade = 'F'

score = input("Enter your score: ")
score = float(score)

if score < 50:
    grade = 'F'
elif score < 60:
    grade = 'D'
elif score < 70:
    grade = 'C'
elif score < 80:
    grade = 'B'
else:
    score > 90
    grade = 'A'









print("Your grade => {}".format(grade))

