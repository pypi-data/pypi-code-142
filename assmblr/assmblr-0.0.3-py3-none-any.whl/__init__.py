from strict import *

if __name__ == "__main__":
    from dataclasses import dataclass
    import re
    import datetime

    is_str_predicate = StrictPredicate | (lambda x: isinstance(x, str))
    is_non_empty = StrictPredicate | (lambda x: len(x) > 0)
    is_str_non_empty = is_str_predicate | is_non_empty

    is_age_adult = (
        StrictPredicate | (lambda x: isinstance(x, int)) | (lambda x: x >= 18)
    )
    is_name = is_str_non_empty | re.compile(r"^[a-zA-Z ]+$").match
    is_email = (
        is_str_non_empty
        | re.compile(r"^([a-zA-Z0-9_\-.]+)@([a-zA-Z0-9_\-.]+)\.([a-zA-Z]{2,5})$").match
    )
    is_phone = is_str_non_empty | re.compile(r"^\\+(?:[0-9] ?){6,14}[0-9]$").match

    is_card_number = is_str_non_empty | re.compile(r"^[0-9]{16}$").match
    is_card_cvv = is_str_non_empty | re.compile(r"^[0-9]{3}$").match
    is_card_expiry = (
        is_str_non_empty
        | re.compile(r"^[0-9]{2}/[0-9]{2}$").match
        | (lambda x: datetime.datetime.strptime(x, "%m/%y") > datetime.datetime.now())
    )

    # using dataclasses cause quick and easy to instantiate, but this works for standard classes too, you just have
    # to assign values in the init like normal (don't assign a Descriptor object in init, do that on the class level)

    @dataclass
    class Card:
        number = StrictlyDescriptor | is_card_number | "Card number is invalid"
        cvv = StrictlyDescriptor | is_card_cvv | "Card CVV is invalid"
        expiry = StrictlyDescriptor | is_card_expiry | "Card expiry is invalid"

    @dataclass
    class CustomerInfo:
        forename: str = StrictlyDescriptor | is_name | "Must be a non-empty string"
        surname: str = StrictlyDescriptor | is_name | "Must be a non-empty string"
        age: int = (
            StrictlyDescriptor
            | is_age_adult
            | "Must be an integer greater than or equal to 18"
        )

    @dataclass
    class ContactDetails:
        email = StrictlyDescriptor | is_email | "Email is invalid"
        phone = StrictlyDescriptor | is_phone | "Phone is invalid"

    @dataclass
    class Customer:
        customer_info = (
            StrictlyDescriptor
            | (lambda x: isinstance(x, CustomerInfo))
            | "Must be a CustomerInfo object"
        )

        contact_details: ContactDetails = (
            StrictlyDescriptor
            | (lambda x: isinstance(x, ContactDetails))
            | "Must be a ContactDetails object"
        )

        card: Card = (
            StrictlyDescriptor
            | (lambda x: isinstance(x, Card))
            | "Must be a Card object"
        )
