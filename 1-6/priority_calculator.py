def main():
  priority_calculator = (input("공백으로 구분하여 입력하세요 예 4 + 5 * 3 - 2: "))
  priority_calculator= priority_calculator.split(" ")

  priority_calculator = list(filter(None, priority_calculator))
  if priority_calculator == [] :
        return print("Invalid input.") 
  
  #312
 

#   match priority_calculator:
#      case "+","-":
        
        
        
      
  # if priority_calculator.sort():
    
  Operator =  ['+', '-', '*', '/']

  
  parsed_tokens = []
  try:
        for token in priority_calculator:
            if token in Operator:
                parsed_tokens.append(token)
            else:
                # 숫자로 변환 시도 (float)
                parsed_tokens.append(float(token))
        if len(parsed_tokens) < 3 :
            return print("Invalid input.")
        for i in range(len(parsed_tokens) - 1):
            if   parsed_tokens[i] in Operator and parsed_tokens[i+1] == float  :
                return print("Invalid input.")
            
            if  parsed_tokens[i] == "-" and parsed_tokens[i+1] == "-"  and  parsed_tokens[i+2] == "-" :
                parsed_tokens[i:i+2] = '+'                
  
  except ValueError:
    return print("Invalid input.")
  
  def add(NumFirst, NumSecond):
    return NumFirst + NumSecond
  def subtract(NumFirst, NumSecond):
    return NumFirst - NumSecond
  def multiply(NumFirst, NumSecond):
    return NumFirst * NumSecond
  def divide(NumFirst, NumSecond):
    if NumSecond == 0:
      return print("Error: Division by zero.")
    return NumFirst / NumSecond
  i = 0
  while i < len(parsed_tokens):
    if parsed_tokens[i] == '*':
      result = multiply(parsed_tokens[i-1], parsed_tokens[i+1])
      parsed_tokens[i-1:i+2] = [result]
      # 리스트가 변경되었으므로 처음부터 다시 스캔
      i = 0
    elif parsed_tokens[i] == '/':
      # 연산자 앞뒤의 숫자로 나눗셈 수행
      result = divide(parsed_tokens[i-1], parsed_tokens[i+1])
      # [숫자, '/', 숫자] 부분을 계산 결과로 대체
      parsed_tokens[i-1:i+2] = [result]
      i = 0
    else:
      i += 1
  final_result = parsed_tokens[0]
  # 남은 덧셈/뺄셈을 순서대로 계산

  try :
    for i in range(1, len(parsed_tokens), 2):
        operator = parsed_tokens[i]
        next_number = parsed_tokens[i+1]
        if operator == '+':
            final_result = add(final_result, next_number)
        elif operator == '-':
            final_result = subtract(final_result, next_number)
  except IndexError:
     
        return print("Invalid input.")
  if final_result == None :
     return None 
  return print("Result:",final_result )
     
if __name__ == "__main__":
    main()
