from collective.easyform.actions import ActionFactory
from collective.easyform.actions import BaseHandler
from collective.easyform.actions import Mailer
from collective.easyform.interfaces import IMailer
from plone import api
from plone.supermodel.directives import fieldset
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import validator
from collective.easyformplugin.filemailer import _
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid

import sys

# Unused imports but needed if we want to fancy up the pathtomyfile field with a RelationChoice in the future
# from plone.app.z3cform.widget import RelatedItemsFieldWidget
# from z3c.relationfield.schema import RelationChoice
# from plone.app.vocabularies.catalog import StaticCatalogVocabulary
# from zeelandia.theme.vocabularies import CatalogSource
# from plone.autoform import directives
# from plone.namedfile.field import NamedBlobFile

def stripleadingslash(value):
    if value.startswith('/'):
        return value[1::]
    return value

MAX_ATTACHMENT_SIZE=1024*1024*8

class IFileMailer(IMailer):


    pathtomyfile = schema.ASCIILine(
        title=_("URL path to a private File in the CMS."),
        description=_("Use the format: /path/to/item . This is most likely a PDF you want to attach. " 
                    "Don't publish the content item if you want to keep it exclusive to form submissions.")
    )

    fieldset(
        u"mailattachment",
        label=_("Attachment"),
        fields=["pathtomyfile"],
    )
    # Leaving these here as a warning: the Schema for an Easyform Action is not a full traversable
    # context in the CMS and gets serialized to/from a plone.supermodel schema, loosing all complex
    # objects
    #
    # myfile = NamedBlobFile(
    #     title="Upload a file",
    #     required=False,
    # )
    # attachfile = RelationChoice(
    #     title=u"Select a file",
    #     description=u"z3c.relationfield.schema.RelationChoice",
    #     vocabulary="zeelandia.catalog",
    #     required=False,
    # )
    # directives.widget(
    #     "attachfile",
    #     RelatedItemsFieldWidget,
    #     pattern_options={"selectableTypes": ["File"],
    #     "basePath": "",
    #     "mode":"search"},
    # )


@implementer(IFileMailer)
class FileMailer(Mailer):

    def __init__(self, **kw):
        # only set attachfile attribute, then call super for the fields in the IMailer interface.
        for i, f in IFileMailer.namesAndDescriptions():
            setattr(self, i, kw.pop(i, f.default))
        super(FileMailer, self).__init__(**kw)



    def get_attachments(self, fields, request):
        attachments = super(FileMailer, self).get_attachments(fields, request)
        myfile = getattr(self,'pathtomyfile', None)

        if myfile:
            myfile = stripleadingslash(myfile)
            portal = api.portal.get()
            try:
                obj = portal.unrestrictedTraverse(myfile)
            except:
                obj = None
        if obj and obj.file:
            attachments.append((obj.file.filename,obj.file.contentType,'utf-8',obj.file.data))
        else:
            messages = IStatusMessage(request)
            messages.add(u"Attachment couldn't be added, please content the website owner", type=u"warn")
        return attachments

class FileAttachmentValidator(validator.SimpleFieldValidator):
    
    def validate(self, value):
        portal = api.portal.get()
        try:
            myfile = portal.unrestrictedTraverse(stripleadingslash(value))
        except:
            raise Invalid(_("File object cannot be found"))
        if not myfile.file:
            raise Invalid(_("File object has no file data"))

        size = sys.getsizeof(myfile.file.data)
        # No cookie if size is bigger than 8Mbyte but in bytes
        if size > MAX_ATTACHMENT_SIZE:
            raise Invalid(_("File is larger than 8 MB, this is too large as an attachment to E-mails."))

validator.WidgetValidatorDiscriminators(
    FileAttachmentValidator, field=IFileMailer["pathtomyfile"]
)

FileMailerAction = ActionFactory(
    FileMailer,
    _(u"label_mailer_action", default=u"File Mailer"),
    "collective.easyform.AddMailers",
)

FileMailerHandler = BaseHandler(FileMailer)
