num = int(input("Enter a number: "))
temp = num
count = 0
sum = 0

# Count digits
while temp > 0:
    temp = temp // 10
    count += 1

temp = num

# Calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")