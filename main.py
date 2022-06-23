from app.calculator.calculator import Calculator


def main():
    with open("example1.txt") as f:
        example1 = f.read()

    with open("example2.txt") as f:
        example2 = f.read()

    cal = Calculator(example1)
    print(f"The amount to pay {cal.name} is: {cal.calculate_amount()} USD")

    cal = Calculator(example2)
    print(f"The amount to pay {cal.name} is: {cal.calculate_amount()} USD")


if __name__ == '__main__':
    main()
