#
# FILE: if_one.py
# TASK: lab_06
# LANG: PYTHON
# ID:   6810620044
#

#
# Create if statement with one alternative.
#

# Assume the following variables
x, y, z = float(), float(), float()

j, k, m, n = int(), int(), int(), int()
m_length, max_length = int(), int()

flag, error = bool(), bool()

ch = str()   ## single character

# store result of a condition
cond = bool()

# 1. if x is greater than y then assign x to z
if x > y:
    z = x




# 2. if y is not zero and flag is not False then assign x divided by y to z
cond = (y != 0 and flag != False)
if cond:
    z = x / y




# 3. if n is not zero and m is divisible by n then set flag to True
cond = (n != 0 and m % n ==0)
if cond:
    flag = True




# 4. if x and y are both positive then set flag to True
cond = (x > 0) and (y > 0)
if cond:
    flag = True




# 5. if m_length is positive and less than max_length then set both m and n to zero
cond = (m_length > 0) and (m_length < max_length)
if cond:
    m = 0
    n = 0



# 6. if j and k are not the same then set n to the remainder of dividing j by k





# 7. if x and y are both negative then set error to True
cond = (x < 0) and (y < 0)
if cond:
    error = True




# 8. if j is not between m and n (inclusive and assume m is less than n) then set k to zero
cond = (j > n) or (j < m)
if cond:
    k = 0




# 9. if m_length is positive and less than max_length and ch is a lowercase letter then set flag to True
cond = 0 <= m_length < max_length and ch.islower()
if cond:
    flag = True




# 10. if m_length is positive and less than max_length and ch is a decimal digit ('0' to '9') then set flag to True
cond = 0 <= m_length < max_length and ch.isdecimal()
if cond:
    flag = True





