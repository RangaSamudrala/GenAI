import sys

def basic_calculator_with_operation(num1, num2, operation = "*"):
  if operation == "+":
    return num1 + num2 
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2 
  elif operation == "/":
    if num2 == 0:
        return "Zero division error"
    return num1 / num2
  else:
    return "Error: Unsupported operation"

print("Before main...")
if __name__ == '__main__':
  n1 = float(sys.argv[1])
  n2 = float(sys.argv[2])
  op = sys.argv[3]

  result = basic_calculator_with_operation(n1, n2, op)
  print(f"Result: {result}")

print("After main...")
