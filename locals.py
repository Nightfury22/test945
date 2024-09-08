y = 20
def myfunc():
    z = 30
    x = 20
    return locals()
print(myfunc())