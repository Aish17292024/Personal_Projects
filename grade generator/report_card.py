num_student = int(input("How many students do you want to enter? "))
all_results = []

class student():
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def avg(self):
		total = sum(self.marks)
		average = total / len(self.marks)
		result = (f"\nHello {self.name}!")
		result += (f"\nYour average marks are = {average}")
		result += self.grade(average)
		print(result)
		return result

	def grade(self, average):
		if(average >= 90):
			return("\nYour grade is: A+! Excellent🌟")
		elif(average >= 80):
			return("\nYour garde is: A! Very Good✨")
		elif(average >= 70):
			return("\nYour grade is: B! Keep it up😇")
		elif(average >= 60):
			return("\nYour grade is: C! Need to work hard📚")
		elif(average >= 40):
			return("\nYour grade is: D! Please improve😕")
		else:
			return("\nYour grade is: F! You have to study harder🤕")


for i in range(0,num_student):
	print(f"\n🗒️ Entering the details of the student {i+1}....")
	name = input("\nEnter name: ")
	marks = list(map(int,input("Enter marks obtained seprated by commas (e.g. 90,82,75): ").split(',')))

	stud = student(name, marks)
	result = stud.avg()
	all_results.append(result)

save = input("\nDo you want to save the result in file? (yes/no): ").lower()
if(save == "yes"):
	with open("Students_result.txt", "w") as f:
		f.writelines(all_results)
	print("Done! Result saved successfully to 'Students_result.txt'✅")
else:
	print("Your result is not saved in file.")

