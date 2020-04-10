# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses.values())
total = sum(courses.values())
print(total)
percentage = total*100 / 500
print(round(percentage))

# Code ends here


# --------------
# Code starts here
names = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Benjio','Hilary Mason','Corinna Cortes','Peter Warden']
scores = [78,95,65,50,70,66,75]
mathematics = dict(zip(names,scores))
topper = max(mathematics,key=mathematics.get)
print(topper)
# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
last_name = topper.split()[1]
first_name = topper.split()[0]
full_name = last_name + " " + first_name
certificate_name = full_name.upper()
# Code ends here


