from firebase import firebase
from time import sleep
import time
firebase = firebase.FirebaseApplication('https://device-control-d49d9-default-rtdb.firebaseio.com/',None)
device = '/device'
led_control = "/led"
fan_control = "/fan"
led_check = 0
fan_check = 0
def main():
	result = firebase.get(device, None)   #Lấy dữ liệu từ firebase về
	print(result)
	a = int(result['led'])
	b = int(result['fan'])
	global led_check
	global fan_check
	if led_check != a:
		led_check = a
		if a == 1:
			led_on()
		else:
			led_off()
	if fan_check != b:
		fan_check =b
		if b == 1:
			fan_on()
		else:
			fan_off()

def led_on():
	result = firebase.put(device, led_control, '1')

	with open('vidu.txt', 'a') as f: #Lưu vào file txt
		f.write("Led on: ")
		f.write(time.ctime())
		f.write("\n")
		f.close()

def led_off():
	result = firebase.put(device, led_control, '0')

	with open('vidu.txt', 'a') as f: #Lưu vào file txt
		f.write("Led off: ")
		f.write(time.ctime())
		f.write("\n")
		f.close()

def fan_on():
	result = firebase.put(device, fan_control, '1')
	with open('vidu.txt', 'a') as f: #Lưu vào file txt
		f.write("fan on: ")
		f.write(time.ctime())
		f.write("\n")
		f.close()

def fan_off():
	result = firebase.put(device, fan_control, '0')
	with open('vidu.txt', 'a') as f: #Lưu vào file txt
		f.write("fan off: ")
		f.write(time.ctime())
		f.write("\n")
		f.close()

if __name__ == "__main__":
	main()