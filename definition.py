# this codes helps to create a funtion that can be called to do the same work

def addProblem(x, y):
    add = x + y
    sentence = "the sum of {} and {} is {}.".format(x, y, add)
    print(sentence)


def name():
    print("Adiza is very inspiring")


def main():
    addProblem(2, 3)
    addProblem(1334439394, 84848888585885)
    a = int(input("enter an integer:"))
    b = int(input("enter another integer:"))
    addProblem(a, b)
    name()
