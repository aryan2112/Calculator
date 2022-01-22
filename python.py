print("CALCULATOR")
print("Type 'quit' to Exit")
run= True
equation=0

def calculate():
    global run
    global previous
    equation = input("Enter equation - ")
    if equation=='quit':
        run=False
    else:
        previous=eval(equation)
        print(previous)
while run:
    calculate()
