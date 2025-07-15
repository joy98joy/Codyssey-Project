def main():
    num = input("숫자들을 공백으로 구분하여 입력하세요 (예: 3 9 1 4 2): ")
    num = num.split(" ")    
    num = list(map(float, num))
    for i in range(len(num)-1):
        swap = False
        for index2 in range(len(num)-i-1):
            if num[index2] > num[index2 +1]:
                num[index2] , num[index2+1] = num[index2+1],num[index2]
                swap = True
    formatted_output = ",".join([f"<{n}>" for n in num])

    return print("Sorted:",formatted_output)
if __name__ == "__main__":
    main()
