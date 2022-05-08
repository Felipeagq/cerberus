from cerberus import Validator

v = Validator()
# allow_unknown viene en False por defecto
print(v.allow_unknown)
# >>> False

# este schema NO acepta valores unknown
# Pero el diccionario interno SI acepta valores unknown
schema = {
    "name": {"type":"string"},
    "a_dict":{
        # settings
        "type":"dict",
        "allow_unknown":True,
        "require_all":True,
        "schema":{ 
            # keys del diccionario
            "address":{"type":"string"}
        }
    }
}
document = {
    "name":"felipe",
    "a_dict":{
        "address":"calle x carrera y",
        "postal":"01800" # un valor unknown
    }
}
print(v(document,schema))
# >>> True
