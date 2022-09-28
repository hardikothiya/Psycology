from rest_framework import serializers
# from app_demo.models import User
from ..models import User


class UserRegSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserRegSerializer, self).__init__(*args, **kwargs)
        self.fields["username"].error_messages["required"] = u"username is required"
        self.fields["username"].error_messages["blank"] = u"username is required"
        self.fields["first_name"].error_messages["blank"] = u"first_name may not be Blank"
        self.fields["last_name"].error_messages["blank"] = u"first_name may not be Blank"
        self.fields["email"].error_messages["required"] = u"email is required"
        self.fields["email"].error_messages["blank"] = u"email may nota be Blank"
        self.fields['gender'].error_messages["blank"] = u"gender may not be Blank"
        self.fields['gender'].error_messages["required"] = u"gender may not be Blank"
        self.fields["password"].error_messages[
            "min_length"
        ] = u"password must be at least 8 chars"
        self.fields['age'],
        self.field['height'],
        self.field['weight']

