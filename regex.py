import re
file=open('regex.txt','r')
text=file.read()
name_pattern = r'M\w*\.\s*\w*'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
url_pattern = r'www.+in|www.+org|www.+com|plus.+com'
phone_pattern = r'\S[^a-zA-Z\n]+\d+\S[^a-zA-Z\n]'
names = re.findall(name_pattern,text)
emails= re.findall(email_pattern,text)
username = re.findall(r'(\S+)@',text)
urls = re.findall(url_pattern,text)
phone = re.findall(phone_pattern,text)
print("User Names : \n" ,names)
print("Email-id : \n",emails)
print("UserName from email-id : \n",username)
print("Urls: \n",urls)
print("Phone Numbers : \n",phone)