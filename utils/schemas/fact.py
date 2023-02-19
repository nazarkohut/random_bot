"""
FACT_SCHEMA is defined here and is used to determine if response received from NINJAS_API is correct.
"""
from cerberus import Validator

FACT_SCHEMA = {
    "fact": {
        "type": "string",
        "required": True,
        "empty": False
    }
}

fact_validator = Validator(FACT_SCHEMA)
