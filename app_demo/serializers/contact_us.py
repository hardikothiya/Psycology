from rest_framework import serializers
from ..models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactUsSerializer, self).__init__(*args, **kwargs)
        self.fields["userid"].error_messages["required"] = u"userid is required"
        self.fields["subject"].error_messages["required"] = u"subject is required"
        self.fields["message"].error_messages["required"] = u"message is required"
