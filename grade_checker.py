grade = int(input("Enter your numeric grade (0_100): "))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B" 
elif grade >= 70:
    letter = "C" 
elif grade >= 60:
   letter = "D"
else:
    letter = "F"
print(f"Your grade is: {letter}")
message = "Congratulation!" if letter in ["A", "B", "C"] else "Keep practicing, you can do this!"
total_for = 0
for i in range(1, 51):
    if i % 2 == 0:
        total_for += i
print(f"The sum of even numbers from 1 to 50 is {total_for}") 
total_while = 0
num = 1
while num <= 50:
   if num % 2 == 0:
      total_while += num
      num += 1
print(f"The sum of even numbers from 1 to 50 is {total_while}")
