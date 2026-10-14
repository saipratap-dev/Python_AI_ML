#Goal: Check camera and server details, find duplicate IP addresses, calculate health status, count warnings and failures, and save a report.
#Version-01: Check one camera
#---------------------------------------------------------------------------------------------------

camera_name = "Gate_01"
ip_address = "192.168.18.01"
server_cpu = 89
camera_online = False

print("Camera Name:", camera_name)
print("IP Adress:", ip_address)

if not camera_online:
  status = "FAILURE"
elif server_cpu >= 80:
  status = "WARNING"
else:
  status = "HEALTHY"

print("Health Status:", status)


#Output
#Camera Name: Gate_01
#IP Adress: 192.168.18.01
#Health Status: FAILURE
