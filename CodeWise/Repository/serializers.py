

from rest_framework import serializers
from Repository.models import QuestionsDb


class QuestionsDbSerializers(serializers.Serializer):

    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(choices=QuestionsDb.LANGUAGE_CHOICES)
    difficulty_level = serializers.ChoiceField(QuestionsDb.DIFFICULTY_CHOICES)
    topic = serializers.CharField(max_length=200)
    score = serializers.IntegerField()
    published_date = serializers.DateTimeField(read_only=True)
    notes = serializers.CharField(max_length=200)
    sample_input = serializers.CharField(max_length=200)
    sample_output = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField(default=True)

class SubmissionSerializer(serializers.Serializer):

    answer = serializers.CharField()
    owner = serializers.CharField()
    question_id = serializers.IntegerField()
    submission_date = serializers.DateTimeField(read_only=True)
    points = serializers.IntegerField(read_only=True)
    remarks = serializers.CharField(read_only=True)




