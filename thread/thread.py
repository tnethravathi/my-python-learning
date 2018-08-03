import time
from threading import Thread, current_thread
#print current_thread().name
print("Hiiii welcome........")
def calc_square(numbers):
	thread_name = current_thread().name
	print("%s : calculating square of a number"%(thread_name))
	for n in numbers:
		time.sleep(1)
		print("%s : square:"%(thread_name),(n*n))
		
def calc_cube(numbers):
	thread_name = current_thread().name
	print("%s : calculating cube of a number"%(thread_name))
	for n in numbers:
		time.sleep(1)
		print("%s : cube:"%(thread_name),(n*n*n))

arr = [1,2,3,4]
t1 = Thread(name='square_thread', target=calc_square, args=(arr,))
t2 = Thread(name='cube_thread', target=calc_cube, args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()

print ("Thankuuuuuuu..............")





