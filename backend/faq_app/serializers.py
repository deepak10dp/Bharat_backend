from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']

    def get_question(self, obj):
        lang = self.context.get('lang', 'en')
        if lang == 'hi':
            return obj.question_hi or obj.question
        elif lang == 'bn':
            return obj.question_bn or obj.question
        return obj.question

    def get_answer(self, obj):
        lang = self.context.get('lang', 'en')
        if lang == 'hi':
            return obj.answer_hi or obj.answer
        elif lang == 'bn':
            return obj.answer_bn or obj.answer
        return obj.answer
