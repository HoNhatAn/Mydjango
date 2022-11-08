import RPi.GPIO as GPIO # Đính kèm thư viện RPi.GPIO vào chương trình
from time import sleep
from firebase import firebase
 
GPIO.setmode(GPIO.BOARD) # Thiết lập kiểu đánh số chân BOARD
GPIO.setmode(GPIO.BCM) # Thiết lập kiểu đánh số chân BCM

Fan1A = 16	#Gắn chân
Fan1B = 18
Fan1E = 22
Led = 11

GPIO.setup(Fan1A,GPIO.OUT)
GPIO.setup(Fan1B,GPIO.OUT)
GPIO.setup(Fan1E,GPIO.OUT)
GPIO.setup(Led,GPIO.OUT) 

firebase = firebase.FirebaseApplication('https://data-46946-default-rtdb.firebaseio.com',None) #Link đến firebase
device = '/device' # dấu / là đường dẫn
led_control = "/led"
fan_control = "/fan"


def led_on():
	print("Turning led on")
	GPIO.output(LED,GPIO.HIGH) #Cấp điện cho chân GPIO
	print ("Led on: ", time.ctime())#In ra cho vui
	
	result = firebase.put(device, led_control, 'On') #Ném lên firebase

	with open('Led.txt', 'a') as f: #Lưu vào file txt
    f.write("Led on: ")
    f.write(time.ctime())
    f.write("\n")
    f.close()

def led_off():

	print("Led off")
	GPIO.output(LED,GPIO.LOW)
	print ("Led off: ", time.ctime())
	
	result = firebase.put(device, led_control, 'Off')

	with open('Led.txt', 'a') as f:
    f.write("Led off: ")
    f.write(time.ctime())
    f.write("\n")
    f.close()

def fan_on():
	print("Turning fan on")
	GPIO.output(Fan1A,GPIO.HIGH)
	GPIO.output(Fan1B,GPIO.LOW)
	GPIO.output(Fan1E,GPIO.HIGH)
	print ("Fan on: ", time.ctime())
	
	result = firebase.put(device, fan_control, 'On')

	with open('Quat.txt', 'a') as f:
    f.write("Fan on: ")
    f.write(time.ctime())
    f.write("\n")
    f.close()

def fan_off():

	print("Fan off")
	GPIO.output(Fan1E,GPIO.LOW)
	print ("Fan off: ", time.ctime())
	
	result = firebase.put(device, fan_control, 'Off')

	with open('Quat.txt', 'a') as f:
    f.write("Fan off: ")
    f.write(time.ctime())
    f.write("\n")
    f.close()

def main()


GPIO.cleanup()

if __name__ == "__main__"
	main()