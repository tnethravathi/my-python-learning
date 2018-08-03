class Employee:
	empcount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empcount += 1

	def displaycount(self):
		print"Total Employee %d"% Employee.empcount

	def employedetails(self):
		print "Name :=" ,self.name,"salary:=",self.salary

obj1 = Employee("Sony",1000)

obj2 = Employee("Tony",2000)

obj1.employedetails()
obj2.employedetails()

obj1.displaycount()
