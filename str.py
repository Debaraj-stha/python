text="hello world!//"

print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.isupper())
print(text.islower())
print(len(text))
print(text.split(' '))#return array of string separated by whitespace
print(text.startswith('H'))
print(text.splitlines())
print(text.title())#return capitalized title

print(text.count('h'))
print(text.encode())
print(text.index('e'))
print(text.casefold())
print(text.lstrip())

x = text.replace("hello", "apples")
print(x)
uri="https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_replace"
url=uri.split(':')
print("url is %s" %(url[1].lstrip("/")))
print(text)
data = {
    "subject": "This is subject",
    "body": "this is body"
  }
res=[]
for key,value in data.items():
    res.append(f"{key}={value}")
print('&'.join(res))
l="Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print(l.splitlines())
