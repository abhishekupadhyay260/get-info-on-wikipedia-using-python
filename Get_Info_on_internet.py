import pywhatkit # to import the module

wiki_search = input("enter the topic name \n") #make sure to right correct spelling as on wikipedia 
lines = input("enter number of lines in which you want information \n") #it will provide information in exact number of lines in which you want

pywhatkit.info(wiki_search, lines) # it will perform google search 
#only search if topic is available on wikipedia

print("\nSuccessfully Searched")
