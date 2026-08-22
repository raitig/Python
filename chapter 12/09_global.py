a = 89
def fun():
    global a #global variable a is declared inside the function
    a = 659
    print(a)

fun()
print(a)
