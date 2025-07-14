def main():
    num = input("숫자들을 공백으로 구분하여 입력하세요 (예: 3 9 1 4 2): ")
    num = num.split(" ")    
    try:
        num = list(map(float, num))

         
    except ValueError:
        return print("Invalid input.")
    num.sort()
    
    return print(f"Min: {num[0]}, Max: {num[-1]}")

        

if __name__ == "__main__":
    main()





