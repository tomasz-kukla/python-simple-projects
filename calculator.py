
class Calc():
    history = []

    @classmethod
    def prin(cls):
        print("History:")
        for e in cls.history:
            print(e)

    @staticmethod
    def add(a,b):
        ans = a+b
        line = f"{ans} = {a} + {b}"
        Calc.history.append(line)
        return ans

    def subs(a, b):
        ans = a - b
        line = f"{ans} = {a} - {b}"
        Calc.history.append(line)
        return ans

    def mul(a, b):
        ans = a * b
        line = f"{ans} = {a} * {b}"
        Calc.history.append(line)
        return ans

    def div(a, b):
        ans = a / b
        line = f"{ans} = {a} / {b}"
        Calc.history.append(line)
        return ans

    def mod(a, b):
        ans = a % b
        line = f"{ans} = {a} % {b}"
        Calc.history.append(line)
        return ans


print("Calculator")
work = bool(1)

while work:

    print("\nWhat do you want to do:")
    print("1.Add 2.Subtract 3.Multiple 4.Divide 5.Modulo 6.Show history 7.Exit")
    try:
        option = int(input("Enter operation number: "))
    finally:
        print(f"Chosen option: {option}")
    if option == 7:
        work = bool(0)
        print("Bye")
        break

    if option != 6:
        try:
            a = float(input("Enter first variable: "))
            b = float(input("Enter second variable: "))
        except Exception:
            print("\tInvalid value")

    if option == 1: print(f'Result: {Calc.add(a, b)}')
    if option == 2: print(f'Result: {Calc.subs(a, b)}')
    if option == 3: print(f'Result: {Calc.mul(a, b)}')
    if option == 4: print(f'Result: {Calc.div(a, b)}')
    if option == 5: print(f'Result: {Calc.mod(a, b)}')
    if option == 6: Calc.prin()








