from validator_collection import validators,errors

x = input("what;s your email address?? ")

try :
    EMAiL_ADDRESS = validators.email(x)
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
else:
    print("Valid")