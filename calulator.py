n1 = float(input("Enter a number: "))
n2 = float(input("Enter a number: "))
print("Enter an operator (+, -, /, *): ")
oper = input()

def calculation(n1, n2, oper):
    if oper == "+":
        a = n1 + n2
        return a,oper
    elif oper == "-":
        a = n1 - n2
        return a,oper     
    elif oper == "*":
        a = n1 * n2
        return a,oper
    elif oper == "/":
        a = n1 / n2
        return a,oper
    else:
        #In this else part it will be executed if the operator selected is incorrect 
        #And The operator will be changed
        print("Wrong Input! Enter Again.")
        oper = str(input())
        return calculation(n1, n2, oper), oper

if __name__ == "__main__":
    a,oper = calculation(n1, n2, oper)
    print(f"{n1} {oper} {n2} = {a}")

