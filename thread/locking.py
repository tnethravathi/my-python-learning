import time 
from threading import Thread, current_thread
print("Hiiii welcome........")

def deposit(balance,lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		balance.value = balance.value +1
		lock.release()
		
def withdraw(balance,lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		balance.value = balance.value -1
		lock.release()

if __name__== '__main__':
	balance = Thread.value('i',200)
	lock = Thread.Lock()
	t1 = Thread(name='deposit_thread', target=deposit, args=(balance,lock))
	t2 = Thread(name='withdraw_thread', target=withdraw, args=(balance,lock))
	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print ("Thankuuuuuuu..............")




