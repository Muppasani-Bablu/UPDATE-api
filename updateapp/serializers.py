from rest_framework import serializers
from updateapp.models import update

class updateserializers(serializers.ModelSerializer):
    class Meta:
        models=update
        fields='__all__'