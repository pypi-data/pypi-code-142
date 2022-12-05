import base64
import mailchimp_transactional as MailchimpTransactional
from .init_creds import mailchimp_key, test
from mailchimp_transactional.api_client import ApiClientError
import iso8601
import typing
from .dates import today_argentina
from .init_creds import init_mongo
from .format import muvi_print

mailchimp = MailchimpTransactional.Client(mailchimp_key)

def send_mail_with_attachment(files_attachments:list, receiver_mail, test_mail="matias@muvinai.com",global_vars:list=list()):
    print("Enviando mail facturacion...")
    attachment = []
    try:
        for file in files_attachments:
            with open(file['path'], 'rb') as f:
                file_str = f.read()
                file_str = base64.b64encode(file_str)
                file_str = file_str.decode('utf-8')
            muvi_print('info', 'Archivo adjunto procesado con exito')
            attachment.append({'content': file_str, 'name': file['name'].split('/')[-1], 'type': 'application/pdf'})
    except:
        return 'error: el archivo no pudo ser encontrado o procesado'
    
    if test:
        to_mail = [{"email": test_mail}]
    else:
        to_mail = [{"email": receiver_mail}]
    
    msg = {
        'from_email': 'no-responder@sportclub.com.ar',
        'from_name': 'SportClub',
        'to': to_mail,
        'global_merge_vars': global_vars,
        'attachments': attachment
    }
    try:
        response = mailchimp.messages.send_template(
            {'template_name': 'facturacion', 'template_content': [], 'message': msg})
        print(response)
        return response[0]
    except ApiClientError as error:
        print('An exception occurred: {}'.format(error.text))
        return 'error'


def send_mail_to_template(receiver: dict, template: str, brand: dict, plan_name: str = "None") -> dict:
    """ Enviar mail con un template determinado

    :param receiver: objeto de cliente del destinatario
    :type receiver: dict
    :param template: nombre del template
    :type template: str
    :param plan: nombre del plan, defaults to "None"
    :type plan: str, optional
    :return: informacion del mail
    :rtype: dict
    """
    try:
        sdate = receiver["last_subscription_date"].strftime("%d/%m/%Y")

    except AttributeError:
        sdate = iso8601.parse_date(receiver["last_subscription_date"]).strftime("%d/%m/%Y")
    except:
        return {}

    global_vars = [{"name": "nombre", "content": receiver["nombre"]},
                   {"name": "apellido", "content": receiver["apellido"]},
                   {"name": "documento", "content": receiver["documento"]},
                   {"name": "plan", "content": plan_name},
                   {"name": "fecha_subscripcion", "content": sdate}
                   ]
    if brand["name"].lower() != "sportclub":
        global_vars.extend([
            {"name": "logo", "content": brand['images']['mail_logo']},
            {"name": "brand_name", "content": brand["name"]}
        ])
    send_mail(receiver["email"], global_vars, template, brand)


def send_alert(reciever_mail: str, proceso: str, mensaje: str, referencia: str, test_mail="matias@muvinai.com") -> typing.Union[dict, None]:
    """ Enviar mensaje de alerta a ignacio@muvinai.com
    :param reciever_mail: email de quien recibe la alerta
    :type reciever_mail: str
    :param proceso: nombre del proceso
    :type proceso: str
    :param mensaje: mensaje
    :type mensaje: str
    :param referencia: referencia
    :type referencia: str
    :return: Respuesta de mailchimp o None en caso de error
    :rtype: dict | None
    """

    global_vars = [{"name": "proceso", "content": proceso},
                   {"name": "mensaje", "content": mensaje},
                   {"name": "referencia", "content": referencia}
                   ]
    brand = {"mail_sender_address": "no-responder@sportclub.com.ar",
            "name": "SportClub"}
    return send_mail(reciever_mail, global_vars, "alertas", brand, test_mail)


def send_mail_inactivo(receiver, brand):
    """ Enviar mail indicando al cliente que está inactivo.

        :param receiver: documento de cliente del destinatario
        :type receiver: dict
        :return: informacion del mail
        :rtype: dict
        """

    global_vars = [{"name": "nombre", "content": receiver["nombre"]}]
    if brand["name"].lower() == "sportclub":
        template = "inactivo"
    elif brand["name"].lower() == "aranceles":
        return
    else:
        template = "inactivo-nosc"
        global_vars.extend([
            {"name": "logo", "content": brand["images"]["mail_logo"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])
    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail(receiver_mail, params, template, brand, test_mail="ignacio@muvinai.com"):
    """ Estructura y envía mail

    :param receiver_mail: mail del receptor
    :type receiver_mail: str
    :param params: lista de objetos que son parámetros a pasar al template
    :type params: list
    :param template: nombre del template
    :type template: str
    :param test_mail: mail del receptor en caso de test
    :type receiver_mail: str
    :return: informacion del mail
    :rtype: dict
    """
    print("Enviando mail" + template)

    msg = {
        "from_email": brand["mail_sender_address"],
        "from_name": brand["name"],
        "to": [{"email": test_mail}] if test else [{"email": receiver_mail}],
        "global_merge_vars": params}

    try:
        response = mailchimp.messages.send_template(
            {"template_name": template, "template_content": [], "message": msg})
        print(response)
        return response[0]
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return {}


def send_mail_cambio_tarjeta(receiver, brand):
    """ Enviar mail indicando al cliente que debe cambiar la tarjeta.

            :param receiver: documento de cliente del destinatario
            :type receiver: dict
            :return: informacion del mail
            :rtype: dict
            """
    fecha_vigencia = receiver["fecha_vigencia"].strftime("%d/%m/%Y")
    global_vars = [{"name": "nombre", "content": receiver["nombre"]},
                   {"name": "fecha_vigencia", "content": fecha_vigencia},
                   {"name": "email_contacto", "content": brand["email_contacto"]}
                   ]

    if brand["name"].lower() == "sportclub":
        template = "pago-rechazado"
    elif brand["name"].lower() == "aranceles":
        return
    elif brand["name"].upper() == "AON":
        template = "cambio_de_tarjeta_aon"
        global_vars = [
            {'name':'nombre','content':receiver['name']},
        ]
    else:
        template = "pago-rechazado-nosc"
        global_vars.extend([
            {"name": "horizontal_white", "content": brand['images']["horizontal_white"]},
            {"name": "image_dark", "content": brand['images']["image_dark"]},
            {"name": "image_light", "content": brand['images']["image_light"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])

    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_bienvenida(receiver, plan, brand, test_mail="ignacio@muvinai.com"):
    """ Enviar mail de bienvenida a la suscripción.

            :param receiver: documento de cliente del destinatario
            :type receiver: dict
            :return: informacion del mail
            :rtype: dict
            """

    global_vars = [{"name": "nombre", "content": receiver["nombre"]},
                   {"name": "apellido", "content": receiver["apellido"]},
                   {"name": "documento", "content": receiver["documento"]},
                   {"name": "plan", "content": plan["name"]},
                   {"name": "fecha_subscripcion", "content": today_argentina().strftime("%d/%m/%Y")},
                   ]

    if plan["sede_local"]:
        db = init_mongo()
        sede = db.club.find_one({"_id": plan["sede_local"]})
        global_vars.extend([
            {"name": "direccion", "content": sede["direccion"]},
            {"name": "telefono", "content": sede["telefono"]},
            {"name": "contact-email", "content": sede["contact-email"]}
        ])
        if "instagram" in sede.keys():
            global_vars.append({"name": "instagram", "content": sede["instagram"]})

    if brand["name"].lower() == 'sportclub':
        if plan["nivel_de_acceso"] == "Full" or plan["nivel_de_acceso"] == "Flex":
            template = "workclub-bienvenida"
        elif plan["nivel_de_acceso"] == "Local":
            template = "bienvenida-local"
        else:
            template = "bienvenida"
    else:
        template = "bienvenida-nosc"
        global_vars.extend([
            {"name": "logo_mails", "content": brand['images']['mail_logo']},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])

    return send_mail(receiver["email"], global_vars, template, brand, test_mail)


def send_mail_exitoso(receiver, plan, brand):
    global_vars = [{"name": "nombre", "content": receiver["nombre"]},
                   {"name": "apellido", "content": receiver["apellido"]},
                   {"name": "plan", "content": plan["name"]},
                   {"name": "fecha_subscripcion", "content": today_argentina().strftime("%d/%m/%Y")}
                   ]

    if brand["name"].lower() == "sportclub":
        template = "exitoso"
    else:
        template = "exitoso-nosc"
        global_vars.extend([
            {"name": "logo_mails", "content": brand['images']["mail_logo"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])

    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_checkout_rechazado(receiver, plan, brand):
    global_vars = [
        {"name": "nombre", "content": receiver["nombre"]},
        {"name": "slug", "content": plan["slug"]},
        {"name": "email_contacto", "content": brand["email_contacto"]}
    ]

    if brand["name"].lower() == "sportlub":
        template = "checkout-rechazado"
    else:
        template = "checkout-rechazado-nosc"
        global_vars.extend([
            {"name": "logo_mails", "content": brand['images']["mail_logo"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])

    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_pago_en_efectivo(receiver, brand, final_price, plan_name):
    """ Estructura y envía mail
    :param receiver_mail: mail del receptor
    :type receiver_mail: str
    :param test_mail: mail del receptor en caso de test
    :type receiver_mail: str
    :return: informacion del mail
    :rtype: dict
    """
    global_vars = [
        {
            "name": "nombre",
            "content": receiver["nombre"],
        }, {
            "name": "precio_total",
            "content": final_price
        }, {
            "name": "plan",
            "content": plan_name
        }
    ]
    if brand["name"].lower() == "sportclub":
        template = "nueva-boleta"
    else:
        template = "nueva-boleta-nosc"
        global_vars.extend([
            {"name": "logo", "content": brand['images']["mail_logo"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])
    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_pago_pendiente(receiver, brand, test_mail="ignacio@muvinai.com"):
    """ Estructura y envía mail
        :param receiver_mail: mail del receptor
        :type receiver_mail: str
        :param test_mail: mail del receptor en caso de test
        :type receiver_mail: str
        :return: informacion del mail
        :rtype: dict
        """

    global_vars = [{"name": "nombre", "content": receiver["nombre"]}]
    if brand["name"].lower() == "sportclub":
        template = "pago-pendiente"
    else:
        template = "pago-pendiente-nosc"
        global_vars.extend([
            {"name": "logo", "content": brand['images']["mail_logo"]},
            {"name": "brand_name", "content": brand["name"]},
            {"name": "email_contacto", "content": brand["email_contacto"]}
        ])
    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_cambio_tarjeta_aon(receiver, brand):
    """ Enviar mail indicando al cliente que debe cambiar la tarjeta.

            :param receiver: documento de cliente del destinatario
            :type receiver: dict
            :return: informacion del mail
            :rtype: dict
            """
    template = "cambio-de-tarjeta-aon"
    global_vars = [
        {'name':'nombre','content':receiver['name']},
    ]

    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_vencimiento_anual(receiver, brand):
    """ Enviar mail indicando al cliente que debe cambiar la tarjeta.

            :param receiver: documento de cliente del destinatario
            :type receiver: dict
            :return: informacion del mail
            :rtype: dict
            """
    template = "vencimiento-anual"
    global_vars = [
        {"name": "nombre", "content": receiver["nombre"]},
        {"name": "apellido", "content": receiver["apellido"]},
        {"name": "plan", "content": receiver["plan"]["name"]},
        {"name": "fecha_vigencia", "content": receiver["fecha_vigencia"].strftime("%d/%m/%Y")},
    ]
    return send_mail(receiver["email"], global_vars, template, brand)


def send_mail_cambio_plan_herenecia(receiver, brand):
    """ Estructura y envía mail
        :param receiver_mail: mail del receptor
        :type receiver_mail: str
        :param test_mail: mail del receptor en caso de test
        :type receiver_mail: str
        :return: informacion del mail
        :rtype: dict
        """
    template = "vencimiento-anual-herencia"
    global_vars = [
        {"name": "nombre", "content": receiver["nombre"]},
        {"name": "apellido", "content": receiver["apellido"]},
        {"name": "precio_mensual", "content": receiver["plan"]['price']},
        {"name": "plan", "content": receiver["plan"]["name"]},
        {"name": "plan_herencia", "content": receiver["plan_herencia"]["name"]},
        {"name": "fecha_vigencia", "content": receiver["fecha_vigencia"].strftime("%d/%m/%Y")},
        {"name": "precio_plan_herencia", "content": receiver['plan_herencia']['price']},
        {"name": "frecuencia", "content": receiver['plan_herencia']['cobro'].lower()}
    ]
    return send_mail(receiver["email"], global_vars, template, brand)
