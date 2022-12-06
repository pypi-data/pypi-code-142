from rest_framework import serializers
from wagtail.documents import get_document_model

class DocumentSerializer(serializers.ModelSerializer):
    document = serializers.SerializerMethodField('create_doc')

    class Meta:
        model = get_document_model()
        fields = ['document',]

    def create_doc(self, data):
        return {
            'id': data.id,
            'title': data.title,
            'contentType': data.content_type,
            'size': data.file.size,
            'url' : data.file.url,
            'ext': data.file_extension,
            'filename': data.filename
        }
