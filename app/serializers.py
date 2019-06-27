from .models import detailmodel
from rest_framework import serializers


class DetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = detailmodel
        fields = ('event','token', 'uid' ,"contact_name" , "contact_uid" , "contact_type" , "message_dtm","message_uid"	,"message_cuid" , "message_dir" , "message_type" , "message_body" , "ack")


