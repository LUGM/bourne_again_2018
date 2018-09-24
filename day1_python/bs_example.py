from bs4 import BeautifulSoup

f = open('index.html');
soup = BeautifulSoup(f, 'lxml')
f.close();

print(soup.prettify()) # printing the html file in a readable format

print("\nTitle tag\n")
print(soup.title) # accessing tags

print("\nAttributes of 'a' tag\n")
print(soup.a.attrs) # listing all attributes

print("\n'id' attribute of 'a' tag\n")
print(soup.a['id']) # accessing an attribute

print("\nTags having class 'sister'\n")
print(soup.find_all(class_='sister')) # finding by class

print("\nTags having id 'link2'\n")
print(soup.find_all(id='link2')) # finding by id
