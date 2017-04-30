from django.contrib import admin
from Tree.models import *
# Register your models here.


class NodeAdmin(admin.ModelAdmin):
    list_display = ('pk','node_name','parent','complete')


class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('pk','homework','prompt')


admin.site.register(Homework)
admin.site.register(Material)
admin.site.register(Node,NodeAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ChoiceQuestion)
admin.site.register(TextQuestion,TextQuestionAdmin)
admin.site.register(ChoiceAnswer)
admin.site.register(TextAnswer)