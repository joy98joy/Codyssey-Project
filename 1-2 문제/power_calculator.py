
def main():
  
  
  try:
    num= float(input("Enter number: "))
  except ValueError:
    return print("Invalid number input.")
  
  try:
    exponent = int(input("Enter exponent: "))
  except ValueError:
    return print ("Invalid exponent input.")
  if num < 0 and exponent == 0:
    return print("Result:",-1.0) 
  if exponent == 0:
    return print("Result:",1.0)

  result = 1.0
  if exponent > 0:
    for i in range(exponent):
      result *= num
  
  
  else:
    if num == 0:
      return print("Infinity")
    for i in range(abs(exponent)):
      result *=num
    result = 1.0 /result

  return print("Result:",result)

if __name__ == "__main__":
    main()


    
