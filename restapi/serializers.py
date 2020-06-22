from rest_framework import serializers

from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']
    """def validate_<field_name>(self, value)"""
    def validate_content(self, value):
        if len(value)>100:
            raise serializers.ValidationError("This is way too long")
        return value
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if image is None and content is None:
            raise serializers.ValidationError('Content or image is required')
        return data