from rest_framework import serializers
from Tree.models import *


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        fields = ('prompt','pk')
        read_only_fields = ('pk',)


class ChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = ('prompt','A','B','C','D','pk')
        read_only_fields = ('pk',)


class HomeworkSerializer(serializers.ModelSerializer):
    choice_questions = ChoiceQuestionSerializer(many=True,read_only=True)
    text_questions = TextQuestionSerializer(many=True,read_only=True)

    class Meta:
        model = Homework
        fields = ('homework_name','choice_questions','text_questions','pk')
        read_only_fields = ('pk',)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('material_file','pk')
        read_only_fields = ('pk',)


class NodeSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True,read_only=True)
    homework = HomeworkSerializer(many=True,read_only=True)

    class Meta:
        model = Node
        fields = ('complete','node_name','materials','homework','pk')
        read_only_fields = ('pk',)


class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnswer
        fields = ('answer','student','question','pk')
        read_only_fields = ('pk',)


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = ('answer','student','question','pk')
        read_only_fields = ('pk',)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_id','teacher_name','teacher_password','pk')
        read_only_fields = ('pk',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id','student_name','student_password','pk')
        read_only_fields = ('pk',)


