a = int(input("Please input a number: "))
b = int(input("Please input another number: "))
c = str(input("Input the operation: "))
answer = 0

if c == "+":
    answer = a + b
elif c == "-":
    answer = a - b
elif c == "*":
    answer = a*b
elif c == "/":
    answer = a/b

print(answer)
