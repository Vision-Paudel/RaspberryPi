f= open("Connect.sh", "w+") # Create file with write and append permission
# Initialize variables
h = -999;
t = -999;
c = -999;
while 1: # Loops until it gets all three data.
if(ser.in_waiting >0):
line = ser.readline()
print(line)
if (line[0] == 'h' and h == -999):
h = float(line[1:]) # Get humidity
if (line[0] == 't' and t == -999):
t = float(line[1:]) # Get temperature
if (line[0] == 'c' and c == -999):
c = float(line[1:]) # Get light
if ('h' != -999 and 't' != -999 and c != -999): # Print("Humidity is: " + str(h) +"\nTemperature is: " + str(t) +"\nC is: " + str(c)) for debugging purposes!
break
f.write("echo \"use raspberrypi\" > runnable.sql\n") # change to your database name.
f.write("echo \"INSERT INTO SensorData (Time, Temperature, Humidity, Light) VALUES (NOW()," + str(t) + ", " + str(h) + ", " + str(c) + ");\" >> runnable.sql\n")
f.write("echo \"quit\" >> runnable.sql\n")
f.write("echo mysql -u raspberrypi -p mypassword < runnable.sql'\n")
f.write("exit")
f.close() # Close file.
