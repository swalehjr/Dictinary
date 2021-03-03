student = {
"FName" : "James",
"Lname" : "Bond",
"Phone" : 722806931,
"Email" :"Jamesbond@gmail.com"
}
print(student)

car= {
  "brand" : "Ford",
  "electric" : "false",
  "year" : 2015,
  "colors" : ["red","white","blue"]
}
print(car)

car = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964,
}
x = car["model"]
y = car["brand"]
z = car["year"]
print (x)
print (y)
print(z)


car = {
"brand" : "Wagon",
"model" : "Bugatti",
"year" : "1964",
}
if "model" in car:
  print("Yes,'model' is one of the keys in the thisdict dictionary")


car = {
"brand" : "bugatti",
"model" : "wagon",
"year" : "1964",
}
car["year"] = 2018
print(car)
