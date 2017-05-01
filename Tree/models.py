from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100,primary_key=True)
    student_password = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=100,primary_key=True)
    teacher_password = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name


class Node(MPTTModel):
    complete = models.BooleanField(default=False)
    node_name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.node_name


class Homework(models.Model):
    node = models.ForeignKey(Node,related_name='homework',on_delete=models.CASCADE)
    homework_name = models.CharField(max_length=100)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.homework_name


class TextQuestion(models.Model):
    homework = models.ForeignKey(Homework,related_name='text_questions',on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    prompt = models.CharField(max_length=100)
    choice_question = models.BooleanField(default=False)

    def __str__(self):
        return self.prompt+'pk:'+str(self.pk)


class ChoiceQuestion(models.Model):
    homework = models.ForeignKey(Homework,related_name='choice_questions',on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    prompt = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    choice_question = models.BooleanField(default=True)

    def __str__(self):
        return self.prompt+'pk:'+str(self.pk)


class TextAnswer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    question = models.ForeignKey(TextQuestion,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer+'pk:'+str(self.pk)


class ChoiceAnswer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    question = models.ForeignKey(ChoiceQuestion,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer+'pk:'+str(self.pk)


class Material(models.Model):
    material_name = models.CharField(max_length=100,null=True)
    node = models.ForeignKey(Node,related_name='materials',on_delete=models.CASCADE)
    material_file = models.FileField(upload_to="materials/")

    def __str__(self):
        return 'pk:'+str(self.pk)



