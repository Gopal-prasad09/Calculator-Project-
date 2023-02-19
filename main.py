a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
while True:
  r = input("Enter your choice (+,-,*,/) : ")
  print()
  if r == '+':
    print(a + b)
    print()
    input("Press ENTER to continue")
    print()
  elif r == '-':
    print(a - b)
    print()
    input("Press ENTER to continue")
    print()
  elif r == '*':
    print(a * b)
    print()
    input("Press ENTER to continue")
    print()
  elif r == '/':
    print(a / b)
    print()
    input("Press ENTER to continue")
    print()
  else:
    print('Invalid Choice')
    break