
def calculator():
  NumFirst = input("Enter number: ")
  Operator = input("Enter operator(+, -, *, /): ")
  NumSecond= input("Enter number: ")
  
  
  NumFirst = int(NumFirst)
  NumSecond = int(NumSecond)

  if NumSecond == 0:
    return print("Error: Division by zero.")
  #finsh
  
  def add(NumFirst, NumSecond):
    return NumFirst + NumSecond
  def subtract(NumFirst, NumSecond):
    return NumFirst - NumSecond
  def multiply(NumFirst, NumSecond):
    return NumFirst * NumSecond
  def divide(NumFirst, NumSecond):
    return NumFirst / NumSecond
  if Operator not in ['+', '-', '*', '/']:    
    return print("Invalid operator.")
  
  elif Operator == '+':
    result = add(NumFirst, NumSecond)
  elif Operator == '-':
    subtract(NumFirst, NumSecond)
  elif Operator == '*':
    multiply(NumFirst, NumSecond)
  elif Operator == '/':
    divide(NumFirst, NumSecond)

  return print(f"Result: {result}")


if __name__ == "__main__":
  calculator()
