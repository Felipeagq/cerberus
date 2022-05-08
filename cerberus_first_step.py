from cerberus import Validator
v = Validator()

# Validaciones de tipo de datos
schema = {"name":{"type":"string"}}
document = {"name":"felipe"}
print(v.validate(document,schema),end="\n\n")
# >>> True


# Validaciones tipo de datos y valor minimo
schema = {
    "name":{"type":"string"},
    "age":{
        "type":"integer",
        "min":30
    }
}
document={
    "name":"felipe",
    "age":23
}
print(v.validate(document,schema),end="\n\n")
# >>> False



# Tambien se puede llamar sin el ".validate"
print(v(document,schema),end="\n\n")
# >>> False


# Por defecto, se tiene en cuenta las llaves definidas en el schema
document = {
    "name":"felipe",
    "age":33,
    "sex":"M"
}
print(v(document,schema))
# >>> False
print(v.errors) # no salta excepción
# >>> {'sex': ['unknown field']}
# Pero podemos hacer que permita llaves desconocidas
v.allow_unknown  = True
print(v.validate(document,schema))
# >>> True

# podemos declara un schema como un allow_unknown
v.allow_unknown = {"type":"integer"}
print(v(document,schema)) # con el unknown como string
# >>> False
document["sex"] = 1
print(v(document,schema)) # con el unknown como integer
# >>> True


print("*"*50)
schema2 = {
    "name":{
        "type":"string",
        "maxlength":3
    }
}
document ={
    "name":"felipe",
    "sex":"m"
}
print(v(document,schema2))
print(v.errors)