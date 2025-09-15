#
# FILE: if_two.py
# TASK: lab_06
# LANG: PYTHON
# ID:   6810620044
#

#
# Create if statement with two alternatives.
#

# Assume the following variables
x, y, z = float(), float(), float()

j, k, m, n = int(), int(), int(), int()
m_length, max_length = int(), int()

flag, error = bool(), bool()

ch = str()   ## single character

# store result of a condition
cond = bool()

# 1. assign absolute value of difference between x and y to z
if x > y:
    z = x - y
else:
    z = y - x



# 2. if y is not zero and greater than x then set z to x divided by y,
#    otherwise set z to zero
cond = (y != 0 and y > x)
if cond:
    z = x / y
else:
    z = 0


# 3. if m is divisible by n then increment j by 1,
#    otherwise increment k by 1
cond = (m % n) == 0
if cond:
    j += 1
else:
    k += 1


# 4. if x and y are both positive then set m to n,
#    otherwise increment j by 1
cond = (x > 0) and (y > 0)
if cond:
    m = n
else:
    j += 1


# 5. if m_length is positive and m_length is less than max_length then set m to 1,
#    otherwise set error to True
cond =(m_length > 0) and (m_length < max_length)
if cond:
    m = 1
else:
    error = True


# 6. if j is divisible by k then set z to x,
#    otherwise set z to y








# 7. if x is non-zero then multiply x by m and save the result in x,
#    otherwise multiply x by n and save the result in x









# 8. if j is zero then add n to m, otherwise subtract n from m









# 9. if m_length is positive and less than max_length and ch is a lowercase
#    then change ch to its uppercase letter,
#    otherwise set error to True









# 10. if m_length is positive and less than max_length and ch is a decimal digit ('0' to '9')
#     then set n to decimal value (0 to 9) according to the decimal digit,
#     otherwise set error to True










