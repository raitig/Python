# Write a python function to print first n timrs of the following pattern.
''' EX:
    * * *
    * *
    *       For n = 3'''
def pattern(n):
    if (n == 0):
        return
    print("* " * n)
    pattern(n - 1)
pattern(3)