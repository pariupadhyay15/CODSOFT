def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operation={
    "+": add ,
     "-": sub ,
    "*" : mul,
    "/" : div,
}

n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
symbol=input("what operation would you like to perform (+,-,*,/) ")

print( {operation[symbol](n1,n2)})
