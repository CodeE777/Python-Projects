import os, sys, re

myfile = open("Nvidia_2019_10k.txt", "r", encoding = 'utf8')

lines = myfile.readlines()
lines[0:]

for line in lines:
    if re.findall("Tegra", line):
        print(line.strip())


myfile.close()


