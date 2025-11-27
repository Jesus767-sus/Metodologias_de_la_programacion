# Diccionario
"""
Para definir un diccionario se utilizan las llaves {}

Ejemplo de un diccionario vacio
students = {"Name": "Gabriel"}

Los diccionarios son capaces de almacenar una gran cantidad de informacion


"""

student_0 = {"Name","Gabriel"}
student_1 = {"student","Cecya","age","18"}

# Empty Dictionary
homer_0 = {"color": "yellow", "bag": "maggie-bag", }
print(homer_0)
print(type(homer_0))

marge = {"color": "yellow", "bag": "homer-donut", "hair": "blue", "dress": "green", "mom": True}
gun_0 = {"scar": "yellow-orange", "headshot": 1.5}

## Add elements to a dictionary
homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["z-position"]=10
print(homer_0)

marge["x-position"]=15
marge["y-position"]=25
marge["z-position"]=10
print(marge)

# Modifying an element of a dictionary
alien_0 = {"color": "yellow"}
alien_0["color"] = "Blue"
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 0
alien_0["name"] = "Paul"

print(alien_0)

## Looping thought items
for key, value in alien_0.items():
    print(f"The key {key} has value {value}")

## Looping though keys
for key in alien_0.keys():
    print(key)

## Looping though keys
for value in alien_0.values():
    print(value)

# NESTING
# Listas de diccionarios
# Listas en diccionarios
# Diccionarios en diccionarios

from tokenize import Name


homer_0={"color": "yelow",
    "bag":"homer-donut", 
    "hair": "black",
    "Dress":"casual",}
print(homer_0)
print(type(homer_0))

marge_0={"color": "yelow",
    "bag":"homer-donut",
    "hair": "blue", 
    "Dress":"casual",}
scar_0={"color": "yelow",
    "headshot":1.5,}

print(marge_0["bag"])
print(marge_0["color"])

#agregar elemenosa un diccionario 

homer_0["x-posicion"]=15
homer_0["y-posicion"]=20
homer_0["z-posicion"]=10
print(homer_0)  

alien_2=["color": "blue"] 
alien_2["x-position"]= 0
alien_2["y-position"]= 25
print(alien_2)

Name["name"] = "paul"

for key, value in alien_2.items():
    print(f"the key{key} has value {value}")
    
##lopping thoung keys}
for key in alien_2.keys():
    print(key)

##looping though items
for item in alien_2.items():
    print(item)

## lsitas de dicionarios
convenanst== {
    "convenans_grut",
    "convenans_elite", 
    "convenanst_jackal":
 }
for convenanst in convenans :
    print("\n", convenants),
for key, value in convenants.items():
   print 

# dicionarios en dicionarios
sensor = {
    "temperature":{
        "id":"tamp_1",
        "localitation": "aula 105",
        "value":25,
        "unit" :"porsentaje"
    } ,
   "humedad": {
       "id": "hum_1",
       "location": "aulea 105",
     "value": 39,
   }
}
print(input "temperature our humedad")
print(sensor)

