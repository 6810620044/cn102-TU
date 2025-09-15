#
# FILE: condition.py
# TASK: lab_06
# LANG: PYTHON
# ID:   6810620044
#

#
# Create conditional expressions.
#

# Assume the following variables
age, year = int(), int()                    #age = int(), year = int()
w, x, y, z = int(), int(), int(), int()     
k, n = int(), int()

mark, limit, speed = float(), float(), float()

gender, ch = str(), str()

# variable to store result of a condition
cond = bool()

# 1. check if age is 65 or over
cond = (age >= 65)

# 2. check if gender is 'M'
cond = (gender == 'M')


# 3. check if age is from 18 to 21 inclusive
cond = (18 <= age <= 21)


# 4. check if mark is less than 1.5 and limit is also less than 0.1
cond = (mark < 1.5) and (limit < 0.1)


# 5. check if year is divisible by 4
cond = (year % 4) == 0


# 6. check if speed is not greater than 55
cond = not (speed < 55)


# 7. check if y is greater than x and less than z
cond = (x < y) and (y < z)


# 8. check if w is either equal to 6 or not greater than 3
cond = (w == 6) or not (w < 3)


# 9. check if n is less than -k or greater than +k
cond = (n < -k) or (n > +k)


# 10. check if k is a divisor of n (n is divisible by k)
cond = (k % n) == 0


# 11. check if n is an even number (divisible by 2)
cond = (n % 2) == 0


# 12. check if ch is a lowercase letter
cond = ch.islower()


# 13. check if ch is a lowercase vowel ('a', 'e', 'i', 'o', 'u')
cond = (ch == "a") or (ch == "e") or (ch == "i") or (ch == "o") or (ch == "u")


# 14. check if ch is one of 'Y', 'y', 'N' or 'n'
cond = (ch == "ํY") or (ch == "y") or (ch == "N") or (ch == "n")


# 14. check if ch is a decimal digit ('0' to '9')
cond = ch.isdecimal()


# 15. check if age is below 18 and gender is not 'M'
cond = (age < 18) and (gender != 'M')



