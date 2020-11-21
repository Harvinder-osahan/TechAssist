import os

os.system("tput setaf 3")

print ("\t\t\t...Technology Assistant...\n")

os.system(" espeak-ng 'Hello! How Can I Help You?' ")

os.system("tput setaf 6")
print("\t\t Options Available:\n\t\t 1. Ansible \n\t\t 2. AWS\n\t\t 3. Docker\n\t\t 4. Hadoop\n\t\t 5. LVM and Storage Mgmt\n")
os.system("tput setaf 3")

ch = int(input("\tEnter Your Choice: "))

os.system("tput setaf 7")

if(ch == 1):    
    import Ansible.py
elif(ch == 2):
    import AWS.py
elif(ch == 3):
    import Docker.py
elif(ch ==4):
    import Had.py
elif(ch == 5):
    import LVM.py
else:
    os.system("exit")
