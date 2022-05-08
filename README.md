# Cerberus

## Validation Schemas for string
````python
from cerberus import Validator

schema = {
    "key":{
        "type":"string",
        "maxlength": [int],
        
    }
}

````