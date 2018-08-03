class Student:
	
	def __init__(self,first,last):
		self.firstname = first
		self.lastname = last

	def Name(self,firstname,lastname):
		return self.firstname +" " + self.lastname

class Subjects(Student):
	def __init__(self,first,last,subjname,marks):
		Student.__init__(self,first, last)
		self.subname = subjname
		self.marks = marks
	
	def subjectdetails(self):
		return self.subname + " " + self.marks


x = Student("Mary", "Sony")

y = Subjects("Homer", "Simpson", "maths","77")

print(x.Name(),y.subjectdetails())
print(y.subjectdetails())






        
 
		
