def add(a,b):
  return a +b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a,b):
  return float(a)/float(b)


operations = {
  "+": add,
  "-": sub,
  "x": mul,
  "/": div
}

def calculator():

  ok = False
  
  a = float(input("Please input your first number: "))
  while not ok:
  
    print(f"The first number selected is {a}")
    
    for i in operations:
      print(i)
    
    op = input("Please input the operation that you would like to carry out: ")
    
    b = float(input("Please input the next number: "))
    
    ans = operations[op](a,b)
    
    print(f"{a} {op} {b} = {ans}")
  
    cont = input("Would you like to continue with the same numbers? Y or N:")
    
    if cont.upper() == "Y":
      a = ans
  
    elif cont.upper() == "N":
      check = input("Would you like to restart the calculator? Y or N:")
      if check.upper() == 'Y':
        calculator()
      else:
        ok = True
  
    else:
      print("Invalid input. Please restart the program.")
      ok = True

calculator()