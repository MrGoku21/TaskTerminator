import time
import os

print ("Taskkiller for Windows 7 and above")
print ("It's easy, just put the name of the running program.")
print ("If your computer can't terminate a program this is the best program to use.")
print ("")

while True:
    program = input ("Name of the program (Include filetype, .exe, .jar etc): ")
    os.system("taskkill /f /im "+program);
    print ("[+] Successfully, terminated the task "+program)
    time.sleep(5)
    exit()

    #if program > ".exe":
        #print ("[-] Unsucessfully, tried to close "+program," but didn't manage")
        #print ("[!] Are you sure that you are a adminisistrator on this PC?")
        #print ("[!] Is the program up?")
        #time.sleep(3)
        #exit()
