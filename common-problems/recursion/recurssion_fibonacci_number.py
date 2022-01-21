# There are few cases when recursion is useful
# 1.When we need quick solution over efficient one
# 2.While traversing trees

# In this program we'll find fibonacci sequence of a number

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


print(fib(8))
