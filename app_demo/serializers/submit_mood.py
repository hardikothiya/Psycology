from rest_framework import serializers
from ..models import Mood


class MoodSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Mood
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MoodSerializer, self).__init__(*args, **kwargs)
        self.fields["userid"].error_messages["required"] = u"userid is required"
        self.fields["mood"].error_messages["required"] = u"subject is required"
