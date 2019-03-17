import requests
from bs4 import BeautifulSoup
import time

print(" __  _   ____  _      __ __   ____  _____ __ __ ")
print("|  |/ ] /    || |    |  |  | /    |/ ___/|  |  |")
print("|  ' / |  o  || |    |  |  ||  o  (   \_ |  |  |")
print("|    \ |     || |___ |  _  ||     |\__  ||  _  |")
print("|     ||  _  ||     ||  |  ||  _  |/  \ ||  |  |")
print("|  .  ||  |  ||     ||  |  ||  |  |\    ||  |  |")
print("|__|\_||__|__||_____||__|__||__|__| \___||__|__|")

print("Welcome to Kalhash")
print("NOTE: When creating hashes with hashtoolkit, they will be added to the hashtoolkit database")
print("\n")
def menu():
	print("1) check for reverse MD5 Hash")
	print("2) check for reverse SHA1 Hash")
	print("3) Create MD5 Hash (hashtoolkit)")
	print("4) Create SHA1 Hash (hashtoolkit)")
	print("0) Exit Kalhash")
	


	input  = raw_input("Enter Selection...")
	
	if input == "1":
		try:
			
			md5Text = raw_input("Enter MD5 Hash To Check: ")
			page = requests.get("https://hashtoolkit.com/reverse-hash?hash="+md5Text)
			soup = BeautifulSoup(page.content, 'html.parser')
			td = soup.find_all('td', class_='res-text')[0].get_text()
			print("Results from Hash Toolkit...")
			print(td)
		except Exception:
			
			print("\n")
			print("Reverse hash not found in database")
			print("\n")
		try:

			page = requests.get("https://md5.gromweb.com/?md5="+md5Text)
			soup = BeautifulSoup(page.content, 'html.parser')
			em = soup.find_all('em', class_='long-content string')[0].get_text()
			print("Results from Gromweb...")
			print("\n")
			print(em)
		except Exception:
			
			print("\n")
			print("Reverse hash not found in database")
			print("\n")

			print("\n")
		try:
			page = requests.get("https://www.md5reverse.com/"+md5Text)
			soup = BeautifulSoup(page.content, 'html.parser')
			div = soup.find_all('div', class_='result')[0].get_text()
			print("Results from md5reverse")
			
			print(div)
			input1  = raw_input("Press Enter To Continue...")		
			menu()


		except Exception:
			
			print("\n")
			print("Reverse hash not found in database")
			print("\n")
			print("\n")
				
			menu()
		
	
	elif input == "2":
		try:
	
			sha1Text = raw_input("Enter SHA1 Hash To Check: ")
	
		        page = requests.get("https://hashtoolkit.com/reverse-hash?hash="+sha1Text)
	        	soup = BeautifulSoup(page.content, 'html.parser')
	        	td = soup.find_all('td', class_='res-text')[0].get_text()
	
	        	print(td)
			input1  = raw_input("Press Enter To Continue...")		
			menu()
		except Exception:
			print("\n")
			print("\n")
			print("Reverse hash not found in database")
			print("\n")
			print("\n")
			menu()
	
	elif input == "3":
		try:
		        md5Create = raw_input("Enter text to Hash To MD5: ")
		
		        page = requests.get("https://hashtoolkit.com/reverse-hash?hash="+md5Create)
		        soup = BeautifulSoup(page.content, 'html.parser')
		        td = soup.find_all('td', class_='res-hash')[0].get_text()
		
		        print(td)
			input1  = raw_input("Press Enter To Continue...")		
			menu()
		except Exception:
			print("\n")
			print("\n")
			print("Error creating hash.\nText must be at least 2 characters and contain at least 1 letter")
			print("\n")
			print("\n")
			menu()

	elif input == "4":
		try:
		        md5Create = raw_input("Enter text to Hash To SHA1: ")
		
		        page = requests.get("https://hashtoolkit.com/reverse-hash?hash="+md5Create)
		        soup = BeautifulSoup(page.content, 'html.parser')
		        td = soup.find_all('td', class_='res-hash')[1].get_text()
		
		        print(td)
			input1  = raw_input("Press Enter To Continue...")		
			menu()
		except Exception:
			print("\n")
			print("\n")
			print("Error creating hash.\nText must be at least 2 characters and contain at least 1 letter")
			print("\n")
			print("\n")
			menu()
	elif input == "0":
		exit()
	else:
		print("\n")
		print("Invalid selection")
		print("\n")
		menu()
		input  = raw_input("Enter Selection...")
menu()