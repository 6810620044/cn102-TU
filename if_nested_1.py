#
# FILE: if_nested_1.py
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

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 50:
    grade = 'E'
else: 
    score >= 40
    grade = 'F'









print("Your grade {}".format(grade))

