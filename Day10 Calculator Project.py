
# Adding
def add(n1,n2):
  return n1+n2

# Substract
def substract(n1,n2):
  return n1-n2
# Multiply
def multiply(n1,n2):
  return n1*n2

# Divide
def divide(n1,n2):
  return n1/n2

# Operations
operations ={
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
  
}
# Logo 
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
# Calculator
def calculator():
  num1=float(input("What's the first number? "))
  for operation in operations:
    print(operation)
  decision= True
  while decision:
    operation_symbol=input("Pick an operation :  ")
    num2=float(input("What's the next number? "))
    function=operations[operation_symbol]
    answer=function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice=input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ")
    if choice=='y':
      num1=answer
    else:
      decision=False
      calculator()
calculator()



