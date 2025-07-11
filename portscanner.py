print(r"""
  _____ _  __ _____
 | ____| |/ /| ____|
 |  _| | ' / | |
 | |___| . \ | |___
 |_____|_|\_\|_____|
       By EKC
""")


import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Starting Scan Fort ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Enter Targets To Scan(split then by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)
