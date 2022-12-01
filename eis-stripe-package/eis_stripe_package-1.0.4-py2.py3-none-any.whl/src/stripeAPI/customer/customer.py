import stripe
from common.constants.constants import DATA, DEFAULT_PAYMENT_METHOD, MESSAGE
from common.constants.customer_constants import CITY, COUNTRY, LINE1, \
    LINE2, POSTAL_CODE, STATE
from common.constants.messages import BAD_REQUEST_MESSAGE
from common.constants.stripe_exceptions_constants import GENERATE_CUSTOMER_ADDRESS, \
    STRIPE_BAD_REQUEST, STRIPE_CREATE_CUSTOMER_METHOD, STRIPE_DELETE_CUSTOMER_METHOD, \
    STRIPE_GENERIC, STRIPE_INVALID_REQUEST, STRIPE_INVALID_REQUEST_MESSAGE, STRIPE_MODIFY_CUSTOMER_METHOD
from common.exception_service.custom_exception_handler import CoreBadRequest, \
    CoreGenericException, CoreStripeException
from stripeAPI.customer.utils import generate_full_name


def generate_customer_address(
        city: str = None,
        country: str = None,
        address_line1: str = None,
        address_line2: str = None,
        postal_code: str = None,
        state: str = None):
    try:
        if (address_line1 is None or address_line1 == "") \
                and (address_line2 is None or address_line2 == "") \
                and (postal_code is None or postal_code == "") \
                and (state is None or state == "") \
                and (country is None or country == "") \
                and (city is None or city == ""):
            return None

        return {
            CITY: city,
            COUNTRY: country,
            LINE1: address_line1,
            LINE2: address_line2,
            POSTAL_CODE: postal_code,
            STATE: state
        }

    except Exception as exception:
        raise CoreGenericException(exception_traceback=exception,
                                    exception_code=STRIPE_GENERIC,
                                    method_name=GENERATE_CUSTOMER_ADDRESS)


class StripeCustomer:

    @staticmethod
    def create_stripe_customer(
            stripe_secret_key: str,
            email: str,
            first_name: str,
            last_name: str = None,
            address_line1: str = None,
            address_line2: str = None,
            city: str = None,
            postal_code: str = None,
            state: str = None,
            country: str = None,
            description: str = None,
            phone: str = None,
            metadata: dict = None) -> dict:
        """
        Create new stripe Customer.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type email: string
        :param email: Customer's email address.

        :type first_name: string
        :param first_name: Customer's valid first name (name).

        :type last_name: string
        :param last_name: Customer's last name (surname). If last_name is not provided 
                          then first name is used for the stripe customer name.

        :type address_line1: string
        :param address_line1: Address line 1 (e.g., street, PO Box, or company name).

        :type address_line2: string
        :param address_line2: Address line 2 (e.g., apartment, suite, unit, or building).

        :type city: string
        :param city: City, district, suburb, town, or village.

        :type country: string
        :param country: Two-letter country code
                        <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">
                        (ISO 3166-1 alpha-2)</a>.

        :type postal_code: string
        :param postal_code: ZIP or postal code.

        :type state: string
        :param state: State, county, province, or region.

        :type description: string
        :param description: An arbitrary string attached to the object. 
                            Often useful for displaying to users.

        :type phone: string
        :param phone: phone number with country code.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type: dictionary
        :returns: Returns the customer object if the update succeeded with message.
                  If create parameters are invalid errors will be raised.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(email, str) \
                    or not (isinstance(first_name, str) and first_name.strip() != "") \
                    or not isinstance(last_name, (str, type(None))) \
                    or not isinstance(description, (str, type(None))) \
                    or not isinstance(phone, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(address_line1, (str, type(None))) \
                    or not isinstance(address_line2, (str, type(None))) \
                    or not isinstance(city, (str, type(None))) \
                    or not isinstance(country, (str, type(None))) \
                    or not isinstance(postal_code, (str, type(None))) \
                    or not isinstance(state, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CREATE_CUSTOMER_METHOD)

            address = generate_customer_address(
                city=city,
                country=country,
                address_line1=address_line1,
                address_line2=address_line2,
                postal_code=postal_code,
                state=state
            )
            customer = stripe.Customer.create(
                api_key=stripe_secret_key,
                email=email,
                name=generate_full_name(first_name, last_name),
                address=address,
                description=description,
                phone=phone,
                metadata=metadata
            )

            return {
                MESSAGE: "Stripe customer created successfully.",
                DATA: customer
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_CREATE_CUSTOMER_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code=STRIPE_GENERIC,
                                      method_name=STRIPE_CREATE_CUSTOMER_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_CREATE_CUSTOMER_METHOD)


    @staticmethod
    def modify_stripe_customer(
            stripe_secret_key: str,
            customer_id: str,
            email: str = None,
            first_name: str = None,
            last_name: str = None,
            address_line1: str = None,
            address_line2: str = None,
            city: str = None,
            postal_code: str = None,
            state: str = None,
            country: str = None,
            description: str = None,
            phone: str = None,
            default_payment_method: str = None,
            metadata: dict = None) -> dict:
        """
        Update stripe Customer details.

        For modifying customers address user should pass all address parameters 
        (address_line1, address_line2, city, state, country, postal_code) for 
        proper modification. If any parameter doesn't passed, then method will 
        take default value and set it to None (or null). If all parameters are 
        passed as null string or None, then address dictionary will be None and 
        it will not update any address information.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type customer_id: string
        :param customer_id: Stripe customer id for modifying object.

        :type email: string
        :param email: Customer's email address.

        :type first_name: string
        :param first_name: Customer's valid first (name) name.

        :type last_name: string
        :param last_name: Customer's last name (surname).

        :type address_line1: string
        :param address_line1: Address line 1 (e.g., street, PO Box, or company name).

        :type address_line2: string
        :param address_line2: Address line 2 (e.g., apartment, suite, unit, or building).

        :type city: string
        :param city: City, district, suburb, town, or village.

        :type country: string
        :param country: Two-letter country code
                        <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">
                        (ISO 3166-1 alpha-2)</a>.

        :type postal_code: string
        :param postal_code: ZIP or postal code.

        :type state: string
        :param state: State, county, province, or region.

        :type description: string
        :param description: An arbitrary string attached to the object. 
                            Often useful for displaying to users.

        :type phone: string
        :param phone: phone number with country code.

        :type default_payment_method: string
        :param default_payment_method: Add payment_method id to this field for future payment.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type: dictionary
        :returns: Returns the updated customer object if the update succeeded.
                  If create parameters are invalid errors will be raised.
        """
        try:
            if not isinstance(customer_id, str) \
                    or not isinstance(stripe_secret_key, str) \
                    or not isinstance(email, (str, type(None))) \
                    or not isinstance(first_name, (str, type(None))) \
                    or not isinstance(last_name, (str, type(None))) \
                    or not isinstance(description, (str, type(None))) \
                    or not isinstance(phone, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(address_line1, (str, type(None))) \
                    or not isinstance(address_line2, (str, type(None))) \
                    or not isinstance(city, (str, type(None))) \
                    or not isinstance(country, (str, type(None))) \
                    or not isinstance(postal_code, (str, type(None))) \
                    or not isinstance(state, (str, type(None))) \
                    or not isinstance(default_payment_method, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_MODIFY_CUSTOMER_METHOD)

            address = generate_customer_address(
                city=city,
                state=state,
                country=country,
                address_line1=address_line1,
                address_line2=address_line2,
                postal_code=postal_code
            )
            modified_customer = stripe.Customer.modify(
                api_key=stripe_secret_key,
                sid=customer_id,
                email=email,
                name=generate_full_name(first_name, last_name),
                address=address,
                description=description,
                phone=phone,
                invoice_settings={
                    DEFAULT_PAYMENT_METHOD: default_payment_method,
                },
                metadata=metadata
            )

            return {
                MESSAGE: "Stripe customer modified successfully.",
                DATA: modified_customer
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_traceback=exception,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 method_name=STRIPE_MODIFY_CUSTOMER_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code=STRIPE_GENERIC,
                                      method_name=STRIPE_MODIFY_CUSTOMER_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_BAD_REQUEST,
                                       method_name=STRIPE_MODIFY_CUSTOMER_METHOD)

    @staticmethod
    def delete_stripe_customer(stripe_secret_key: str, customer_id: str) -> dict:
        """
        Delete stripe customer using customer id

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type customer_id: string
        :param customer_id: Stripe customer ID which needs to be deleted permanently.

        :type: dictionary
        :return: returns object of deleted customer.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(customer_id, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_DELETE_CUSTOMER_METHOD)

            deleted_customer = stripe.Customer.delete(
                sid=customer_id,
                api_key=stripe_secret_key
            )

            return {
                MESSAGE: "Stripe customer deleted successfully.",
                DATA: deleted_customer
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreGenericException(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                       exception_traceback=exception,
                                       exception_code=STRIPE_INVALID_REQUEST,
                                       method_name=STRIPE_DELETE_CUSTOMER_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_DELETE_CUSTOMER_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_DELETE_CUSTOMER_METHOD)
