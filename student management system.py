class_1=["Amit sharma","Jaspal singh","Shekhar kumar","Yashoda naik"]
print("class_1 is:",class_1 )
class_2=["Hiten patel","Gauri sharma","Chetan Nitave"]
print("class_2 is: ",class_2)
new_class=class_1+class_2
print("new class is: ",new_class)
new_class.append("Priti patil")
print("updated new_class is:",new_class)
new_class.remove("Yashoda naik")
print("updated new_class is: ",new_class)
print("marks of Jaspal singh are: ")
courses={"math":65,"English":70,"History":80,"Hindi":70,"science":60}
print(courses)
total=0
for i in courses.values():
    total=total+i
print("total marks of Jaspal singh is: ",total)
percentage=(total/500)*100
print("percentage of jaspal singh is: ",percentage)
mathematics={"Amit sharma":78,"Jaspal singh":95,"Shekhar kumar":65,"Hiten patel":50,"Gauri sharma":70,"Chetan Nitave":66,"Priti patil":75}
print("the marks of students in mathematics are:",mathematics)
topper=max(mathematics,key=mathematics.get)
print(topper)
name=topper.split( )
first_name=name[0]
print("first name of topper is:",name[0])
last_name=name[1]
print("last name of topper is:",name[1])
full_name=name[1]+' '+name[0]
print("Full Name is:",full_name)
certificate_name=full_name.upper()
print("The topper in mathematics subject is : ",certificate_name)
