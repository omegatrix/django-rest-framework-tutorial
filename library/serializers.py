from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "publish_date",
            "price",
            "colour",
            "isbn13",
        ]
        extra_kwargs = {
            "publish_date": {"required": False},
            "price": {"required": False},
            "colour": {"required": False},
            "isbn13": {"required": False},
        }
