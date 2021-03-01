class_1=['Amit Sharma','Jaspal Singh','Shekhar Kumar','Yashoda Naik']
class_2=['Hiten Patel','Gauri Sharma','Chetan Nitave']
new_class=class_1+class_2
print("New Class ->\n",new_class)
new_class.append("Priti Patil")
print("\nUpdated class ->\n",new_class)
new_class.remove("Yashoda Naik")
print("\nUpdated class ->\n",new_class)
courses={'Math':65,'English':70,'History':80,'Hindi':70,'Science':60}
total=0
for i in courses.values():
    total=total+i
print("\nTotal -> ",total)
percentage=(total/500)*100
print("\nPercentage -> ",percentage)
mathematics={'Amit Sharma':78,'Jaspal Singh':95,'Shekhar Kumar':65,'Hiten Patel':50,'Gauri Sharma':70,'Chetan Nitave':66,'Priti Patil':75}
topper=max(mathematics, key=(lambda k:mathematics[k]))
l1=topper.split( )
full_name=l1[1]+' '+l1[0]
print("\nFull Name -> ",full_name)
certificate_name=full_name.upper()
print("\nCERTIFICATE NAME -> ",certificate_name)
