from rest_framework import serializers
from jsec.models import Stall,Review,Rating


class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = ('id', 'name', 'photourl', 'description')
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review', 'stall_id', 'name')
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'stall_id', 'name')