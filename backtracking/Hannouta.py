# datastructure and algorithmm in python
#chapter 4 4-14 solution
def move(x, y):
    print("move from " + x + " to "+ y)

def Hanot(x, y, z, n):
    if n==1:
        move(x, z)

    else:
        Hanot(x, z, y, n-1)
        move(x, z)
        Hanot(y, x, z, n-1)


Hanot('a', 'b', 'c', 3)
