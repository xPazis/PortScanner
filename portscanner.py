#!/usr/bin/env python3
#sudo nmap -p- -sS -sU -sV -O {target}

import subprocess

target_ip = input("Provide the target for the port scan: ")
print("Initiating attack at: " + target_ip)

multiple_port_scan = input("Specific port? [y or n]: ")
message = ""
ports = []

if(multiple_port_scan == "n"):
	multiple_port_scan = input("All ports or default? [a or d]: ")
	if(multiple_port_scan == "a"):
		message = "sudo nmap -p- -sV -O " + target_ip
	elif(multiple_port_scan == "d"):
		message = "sudo nmap -sV -O " + target_ip
elif(multiple_port_scan == "y"):
	while(multiple_port_scan == "y"):
		new_port = input("Enter a port to attack: ")
		try:
			new_port = int(new_port)
			if(new_port < 0 or new_port > 65535 or new_port in ports ):
				raise ValueError
			ports.append(new_port)
		except ValueError:
			print("Error")
		multiple_port_scan = input("keep going? [y or n]: ")
	message = "sudo nmap -p "
	list_size = len(ports)
	for i in range(list_size):
		message = message + str(ports[i]) + ","
	message = message[:-1]
	message = message + " -sV -O " + target_ip
else:
	print("Wrong input")
result = subprocess.run(message,shell = True, capture_output = True, text = True, check = True)
print("Successfully ran nmap scan")
print(result.stdout)
