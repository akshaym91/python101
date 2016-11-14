import urllib

def read_text():
	quotes = open('C:\Users\makshay\Documents\Code\Udacity\Python101\ProfanityChecker\movie_quotes.txt')
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	if "true" in output:
		print("Profanity Alert!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Failed to scan the document!")
	connection.close()

read_text()