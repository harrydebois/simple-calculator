def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else None


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Simple calculator CLI')
    parser.add_argument('operation', choices=['add','sub','mul','div'])
    parser.add_argument('a', type=float)
    parser.add_argument('b', type=float)
    args = parser.parse_args()
    if args.operation == 'add':
        print(add(args.a, args.b))
    elif args.operation == 'sub':
        print(subtract(args.a, args.b))
    elif args.operation == 'mul':
        print(multiply(args.a, args.b))
    elif args.operation == 'div':
        result = divide(args.a, args.b)
        print('undefined' if result is None else result)


if __name__ == '__main__':
    main()
