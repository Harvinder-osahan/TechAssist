import os

os.system("tput setaf 6")

print("""\t\t\t AWS Cloud Operations Made Easy\n\t\t\t ______________________________\n""")
os.system("tput setaf 5")

print("""\t\t1.Set up your cloud - configure\n\t\t2.Connect to the instance\n\t\t3.Launch a new instance.""")

os.system("tput setaf 7")

ch = int(input())

if(ch == 1):
    os.system("aws configure")
elif(ch == 2):
    IP = input("Instance IP ")
    path = input("Path ")
    os.system("ssh -l ec2-user {0} -i {1}".format(IP, path))
elif(ch == 3):
    ami = input("ami id ")
    itype = input("Instance Type ")
    cnt = input("Count ")
    key = input("Key Pair ")
    sg = input("SG ")
    sId = input("Subnet Id ")
    os.system("aws ec2 run-instances --image-id {0} --count {1} --instance-type {2} --key-name {3} --security-group-ids {4} --subnet-id {5}".format(ami, cnt, itype, key, sg, sId))
else:
    os.system("exit")


