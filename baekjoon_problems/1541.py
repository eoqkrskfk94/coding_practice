formula = input()
num = []
sym = []
temp = ""
for i in range(len(formula)):
  if formula[i] == '+' or formula[i] == '-':
    num.append(int(temp))
    temp = ""
    sym.append(formula[i])
  elif i == len(formula) - 1:
    temp += formula[i]
    num.append(int(temp))
  else:
    temp += formula[i]
 
#print(num)
##print(sym)

total = num[0]
num.pop(0)

for i in range(len(sym)):
  if sym[i] == '-':
    total -= num[i]
  else:
    if i == 0:
      total += num[i]
    else:
      if sym[i-1] == '-':
        sym[i] = '-'
        total -= num[i]
      else:
        total += num[i]

print(total)


