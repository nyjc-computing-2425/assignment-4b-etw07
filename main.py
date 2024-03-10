stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
error = 0
#validating characters allowed in scientific notation
valid = "0123456789x.-^"
test_valid = stdform
for i in range(len(test_valid)):
  if valid.find(test_valid[i]) == -1:
    error += 1
#ensuring ".", "x", "^" symbols appear only once respectively
lst = [".","x","^"]
for i in lst:
  test_len = stdform.replace(i,"")
  if len(test_len) + 1 != len(stdform):
    error += 1
#validating exponent
pos = stdform.find("x")
mantissa = stdform[0:pos]
exponent = stdform[pos+4:]
if str(float(exponent))[-1] != "0":
  error += 1
#output
if error >= 1:
  print("Error converting to scientific E notation.")
else:
  number = mantissa + "E" + exponent
  print(f"This number in E notation is {number}.")