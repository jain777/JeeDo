import re
from django.core.exceptions import ValidationError
from django.core.validators import  RegexValidator

def check_file_size(value):
    limit = 2*1024*1024
    if(value.size>limit):
        raise ValidationError('File too large.Size should not exceed 2MB')

validator_fn = [
    RegexValidator(r'[A-Z]([A-Z]?)[0-9]{2}([A-Z]?)([A-Z]?)([A-Z]?)[0-9]{3}([0-9]?){4}',
                   "Enter UserName (can include alphabets, "
                   "digits and special characters(@,/,_) ). "
                   ),
]


def regex_validators(value):
    err = None
    for validator in validator_fn:
        try:
            validator(value)
            return value
        except ValidationError as exc:
            err = exc
    raise err