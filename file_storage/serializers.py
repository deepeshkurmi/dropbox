from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file_name', 'created_at', 'size', 'file_type']  # Include 'file' field for file uploads

    # def create(self, validated_data):
    #     file = validated_data.pop('file', None)
    #     instance = super().create(validated_data)
    #     if file:
    #         instance.file_name = file.name
    #         instance.size = file.size
    #         instance.file_type = file.content_type
    #         instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     file = validated_data.pop('file', None)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     if file:
    #         instance.file_name = file.name
    #         instance.size = file.size
    #         instance.file_type = file.content_type
    #     instance.save()
    #     return instance
