import re

file = open("petite_frappe_1.txt").read().splitlines()
flag = ""
for line in file:
	if "value 0" in line:
		pass
	else:
		key = re.findall(r"KEY_[A-Z]",line)
		key = "".join(key)
		flag += key.replace("KEY_","")
print "FCSC{"+flag+"}"
