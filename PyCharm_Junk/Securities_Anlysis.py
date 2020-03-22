import os, sys, re, csv, pprint

myfile = open("Nvidia_2019_10k.txt", "r", encoding = 'utf8')

lines = myfile.readlines()
lines[0:]

line = myfile.readlines()
cnt = 0 
cnt += 1

user_input1 = input("Please type the element(s) you are trying to isolate: ")
user_input2 = input("Are you trying to isolate any other data?: ")
user_input3 = input("Please enter in the keywords in any additional desired data: ")

True == "yes" 
False == "no"

if user_input2 == True:
    
    continue

print("continuing")
    
elif user_input2 == False:
    
    print("data printing" + user_input2)

        break 

else: 

    print(user_input2 and user_input3)



    




with open ('output.txt', 'w', encoding = 'utf8') as new_file:
    txt_writer = csv.writer(new_file, delimiter='-')
    for line in lines:
        if re.findall(user_input1, line, re.IGNORECASE):
            print(line.strip())

    for line in lines:
        if re.findall(user_input2, line,re.IGNORECASE):
            print(line.strip())

    for line in lines:
        if re.findall(user_input3, line,re.IGNORECASE):
            print(line.strip())
        if str("Management’s Discussion and Analysis of Financial Condition and Results of Operations | risk factors")  in line:

                        print("""

                                FOUND

                        """)
                        print("line{}: {}".format(cnt, line.strip()))


print("")
        

#with open('output.txt', 'w') as fp:
    #writer = csv.writer(fp, myfile)
    #writer.writeheader("MD&A and Risk Factors")
    #writer.writerows(line)

 



