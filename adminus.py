#!/usr/bin/python

import requests, sys, time
from colorama import Fore, init

def main ():

	if len (sys.argv) < 2:
		print Fore.RED + '[!]' + Fore.RESET + ' Format: ./adminus.py [file] url'
		return

	init ()	
	GOODS = list ()


	print '''{0}
	  ___ _________  ________ _   _ _   _ _____ 
	 / _ \|  _  \  \/  |_   _| \ | | | | /  ___|
	/ /_\ \ | | | .  . | | | |  \| | | | \ `--. 
	|  _  | | | | |\/| | | | | . ` | | | |`--. \\
	| | | | |/ /| |  | |_| |_| |\  | |_| /\__/ /
	\_| |_/___/ \_|  |_/\___/\_| \_/\___/\____/ 
	{1}
	
	Admin-panel, content search

	{2}[ version 0.3 ]{1}
	{2}[ Coded by DOCTOR_RABB ]{1}	

	'''.format (Fore.MAGENTA, Fore.RESET, Fore.CYAN)
	with open (sys.argv [1] if len (sys.argv) == 3 else 'adminlist', 'r') as adm:
		lines = adm.readlines ()
		print Fore.CYAN + '[*]' + Fore.RESET + ' Total admin variants loaded: ' + str (len (lines))
		for i, n in enumerate (lines):
			print Fore.CYAN + '[*]' + Fore.RESET + ' Trying ' + n.strip ('\n').strip ('\r') + ' | ' + str (i) + '/' + str (len (lines))
			if requests.get (sys.argv [-1] + n.strip ('\n').strip ('\r')).status_code == 200:
				print Fore.GREEN + '[+]' + Fore.RESET + ' Admin: ' + n.strip ('\n').strip ('\r')
				GOODS.append (n.strip ('\n').strip ('\r'))
	adm.close ()
	print
	for i in GOODS: print Fore.GREEN + '[+]' + Fore.RESET + i

if __name__ == '__main__':
	main ()
