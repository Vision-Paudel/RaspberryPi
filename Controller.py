import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

f= open("Connect.sh", "w+")
h = -999;
t = -999;
c = -999;
while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
	print(line)
	if (line[0] == 'h' and h == -999):
		h = float(line[1:])
	if (line[0] == 't' and t == -999):
		t = float(line[1:])
	if (line[0] == 'c' and c == -999):
		c = float(line[1:])
	if ('h' != -999 and 't' != -999 and c != -999):
		#print("Humidity is: " + str(h) +"\nTemperature is: " + str(t) +"\nC is: " + str(c)) for debugging purposes!
		break

f.write("echo \"use vpaudel\" > runnable.sql\n")
f.write("echo \"INSERT INTO SensorData (Time, Temperature, Humidity, Light) VALUES (NOW()," + str(t) + ", " + str(h) + ", " + str(c) + ");\" >> runnable.sql\n")
f.write("echo \"quit\" >> runnable.sql\n")
f.write("scp -i LinuxServer.pem runnable.sql ec2-user@ec2-54-144-148-208.compute-1.amazonaws.com:\n")
f.write("ssh -i LinuxServer.pem ec2-user@ec2-54-144-148-208.compute-1.amazonaws.com 'mysql -u vpaudel -p119690330 < runnable.sql'\n")
f.write("exit")

f.close()
