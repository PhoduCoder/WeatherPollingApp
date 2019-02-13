from bs4 import BeautifulSoup
import requests
import json

#Link of the page that you want to reach
page_link='https://gitsmoke.wordpress.com/'

#This response generally contains the
#status of the HTTP request
#If we print the response object we get this : <Response [200]>
#page_response=requests.get(page_link)

#It is also advisable to implement 
#a timeout feature in this
page_response=requests.get(page_link, timeout=5)

#This prints the content of the repsone
#print(page_response.content)

#Store the content of the webpage 
#and then parse using a HTML parser

page_content=BeautifulSoup(page_response.content,"html.parser")

textcontent=[]

topics=page_content.find_all('a', attrs={"href": "https://gitsmoke.wordpress.com"})

print(topics)

links=page_content.find_all('a')
print(links)
#for link in links:
#	#print(link.attrs.values())
#	json_var=json.dumps(link.attrs)
#	#print (type(json_var))
#	reference=json_var.strip(":")
#	print(reference)
#	#print(json_var["href"])

#for i in range(0,20):
#	topics=page_content.find_all('a')[i].href
#	textcontent.append(topics)

#print (textcontent)

