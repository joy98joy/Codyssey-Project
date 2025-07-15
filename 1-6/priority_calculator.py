
def main():
  priority_calculator = (input("공백으로 구분하여 입력하세요 예 4 + 5 * 3 - 2: "))
  priority_calculator= priority_calculator.split(" ")
  Operator =  ['+', '-', '*', '/']
  parsed_tokens = []

  def add(NumFirst, NumSecond):
    return NumFirst + NumSecond
  def subtract(NumFirst, NumSecond):
    return NumFirst - NumSecond
  def multiply(NumFirst, NumSecond):
    return NumFirst * NumSecond
  def divide(NumFirst, NumSecond):
    if NumSecond == 0:
        raise ZeroDivisionError("Error: Division by zero")
    return NumFirst / NumSecond
  
  try:
        for token in priority_calculator:
            if token in Operator:
                parsed_tokens.append(token)
            else:
                # 숫자로 변환 시도 (float)
                parsed_tokens.append(float(token))
        # if parsed_tokens not in Operator:
        #     return print("Invalid input.")
    # while priority_calculator[num]:
    
     
  except ValueError:
        return print("Invalid input.")
  temp_tokens = []
  i = 0
  while i < len(parsed_tokens):
   
      
    
#   NumFirst = int(NumFirst)
#   NumSecond = int(NumSecond)
#   Operator = input("Enter operator(+, -, *, /): ")
  
  
  
  
  #finsh

  
  
  
 
#   if Operator not in ['+', '-', '*', '/']:    
#     return print("Invalid operator.")
  
#   elif Operator == '+':
#     result = add(NumFirst, NumSecond)
#   elif Operator == '-':
#     result = subtract(NumFirst, NumSecond)
#   elif Operator == '*':
#     result = multiply(NumFirst, NumSecond)
#   elif Operator == '/':
#     if NumSecond == 0:
#       return print("Error: Division by zero.")
#     result = divide(NumFirst, NumSecond)
  
#   print(f"Result:{result}")
   return print(1)




'''
calculator.py를 CLI에서 실행해서 사용자 입력 처리와 출력이 올바른지 확인한다.  
계산기 프로그램은 주어진 4가지 연산자 (+, -, , /)에 대해 정상적으로 작동하며, 잘못된 입력이나 0으로 나누는 경우를 적절히 처리하고 있는가?  
올바른 입력과 예외 상황에 대한 조건 분기와 출력에 대해 제대로 설명할 수 있는가?  
각 연산 기능(add, subtract, multiply, divide)이 함수로 분리되어 있고, 사용자 입력 및 결과 출력이 요구사항대로 구성되어 있는가?  
함수 정의, input() 사용, "Result: ..." 형식의 출력 등 코드에 대해 제대로 설명할 수 있는가?  
코드는 calculator.py라는 파일에 작성되었으며, 실행 가능한 상태로 구조(진입점 포함)가 잘 구성되어 있는가?
→ 파일명, if __name__ == "__main__": 구문, 실행 시 오류 없이 동작하는지 확인한다.'''


if __name__ == "__main__":
    main()
