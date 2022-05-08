from cerberus import Validator

v = Validator()

schema = {
    "amount":{
        "type":"integer",
        "coerce":int
    }
}


# Puede ser convertido a int
document = {"amount":"2"}
print(v(document,schema))
print(v.document)


# No puede ser convertido a int
document = {"amount":"dos"}
print(v(document,schema))
print(v.document)

