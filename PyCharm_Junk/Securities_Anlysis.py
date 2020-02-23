import os, sys, re

myfile = open("Nvidia_2019_10k.txt", "r", encoding = 'utf8')

lines = myfile.readlines()
lines[0:]

for line in lines:
    if re.findall("Tegra", line, re.IGNORECASE):
        print(line.strip())

for line in lines:
    if re.findall("GeForce", line,re.IGNORECASE):
        print(line.strip())

for line in lines:
    if re.findall("Management’s Discussion and Analysis of Financial Condition and Results of Operations", line,re.IGNORECASE):
        print(line.strip())

line = myfile.readlines()
cnt = 0 
cnt += 1

if str("Management’s Discussion and Analysis of Financial Condition and Results of Operations\ risk factors")  in line:

            print("""

                        FOUND

                        """)
            print("line{}: {}".format(cnt, line.strip()))


with open('output.txt', 'w') as fp:
    writer = csv.DictWriter(fp, myfile)
    writer.writeheader()
    writer.writerows(line)

myfile.close()




