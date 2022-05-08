
from cerberus import Validator
v = Validator()

###########
# allowed #
###########
schema = {
    "role":{
        "type":"list",
        "allowed":[
            "FrontEnd",
            "BackEnd",
            "DevOps"
        ]
    }
}
document = {
    "role":["FrontEnd"]
}
print(v.validate(document,schema))
# >>> True

document2 = {
    "role":["FrontEnd","UX/UI"]
}
print(v.validate(document2,schema))
# >>> False
print(v.errors)
# >>> {'role': ["unallowed values ('UX/UI',)"]}



# Tambien aplica para los string
schema = {
    "role":{
        "type":"string",
        "allowed":[
            "FrontEnd",
            "BackEnd",
            "DevOps"
        ]
    }
}
document = {
    "role":"FrontEnd"
}
print(v.validate(document,schema))
# >>> True


# Tambien aplica para los integer
schema = {
    "role":{
        "type":"integer",
        "allowed":[
            1,
            2,
            3
        ]
    }
}
document = {
    "role":2
}
print(v.validate(document,schema))
# >>> True
document = {
    "role":4
}
print(v.validate(document,schema))
# >>> False


##############
# check_with #
##############
def lower_name(field,value,error):
    if  not value.islower():
        error(field,"Must be lower")
        
schema_2 = {
    "name":{
        "type":"string",
        "check_with":lower_name
    }
}
document_2 = {
    "name":"Felipe"
}
v(document_2,schema_2)
# >>> False
print(v.errors)
# >>> {'name': ['Must be lower']}

############
# contains #
############
document = {'states': ['peace', 'love', 'inity']}

schema = {'states': {'contains': 'peace'}}
print(v.validate(document, schema))
# >>> True

schema = {'states': {'contains': 'greed'}}
print(v.validate(document, schema))
# >>> False

schema = {'states': {'contains': ['love', 'inity']}}
print(v.validate(document, schema))
# >>> True

schema = {'states': {'contains': ['love', 'respect']}}
print(v.validate(document, schema))
# >>> False