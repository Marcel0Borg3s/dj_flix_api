from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        if reviews:
            sum_reviews = 0

            for review in reviews:
                sum_reviews += review.stars

            reviews_count = reviews.count()

            return round(sum_reviews / reviews_count, 1)
        
        return "No reviews yet"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("Release date must be 1990 or later.")
        return value
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resume must not exceed 200 characters.")
        return value
    


