from rest_framework import serializers
from core.models import Post

class PostSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        categories = []
        for category in obj.categories.all():
            categories.append(category.name)
        return categories

    class Meta:
        model = Post
        fields = '__all__'
