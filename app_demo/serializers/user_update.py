from rest_framework import serializers
from app_demo.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "gender", "birthdate"]

    def __init__(self, *args, **kwargs):
        super(UserUpdateSerializer, self).__init__(*args, **kwargs)
        self.fields["username"].error_messages["required"] = u"username is required"
        self.fields["username"].error_messages["blank"] = u"username is required"
        self.fields["first_name"].error_messages["blank"] = u"first_name may not be Blank"
        self.fields["last_name"].error_messages["blank"] = u"first_name may not be Blank"
        self.fields['gender'].error_messages["blank"] = u"gender may not be Blank"
        self.fields['gender'].error_messages["required"] = u"gender may not be Blank"
        self.fields['birthdate'].error_messages["required"] = u"gender may not be Blank"
        self.fields['birthdate'].error_messages["blank"] = u"gender may not be Blank"

