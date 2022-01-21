# There are few cases when recursion is useful
# 1.When we need quick solution over efficient one
# 2.While traversing trees

# In this program we'll find factorial of a number
# O(n!) 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
