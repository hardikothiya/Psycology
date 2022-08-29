from rest_framework import serializers
from ..models.user_temp import UserTemp

class UserTempSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UserTemp
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserTempSerializer, self).__init__(*args, **kwargs)
        self.fields["email"].error_messages["required"] = u"email is required"
        self.fields["email"].error_messages["blank"] = u"email may not be Blank"
        self.fields["verification_code"].error_messages["blank"] = u"email may not be Blank"
        self.fields["verification_code"].error_messages["required"] = u"email may not be Blank"


