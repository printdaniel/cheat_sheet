
""" 
Zip is useful function that allows you combine two list easily.
After calling zip, an iteator is returned two lists, easily.
After calling zip, and iterator is returned. In order to see the content 
wrapped insido, we need to fiste convert it to a list.

"""

first_name = ['Joe','Earnst','Thomas','Martin','Charles']
last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']
age = [23, 65, 11, 36, 83]

print(list(zip(first_name,last_name, age)))


# unzip
full_name_list = list(zip(first_name,last_name, age))
nombre, apellido, edad = list(zip(*full_name_list))
print(nombre, apellido, edad)

