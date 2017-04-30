from django.conf.urls import url
from Tree import views


urlpatterns = [
    url(r'^login/student$',views.student_login),
    url(r'^login/teacher$',views.teacher_login),
    url(r'^register/(?P<role>\w+)$',views.register),
    url(r'^get_tree$',views.get_tree),
    url(r'^textquestion/(?P<pk>\w+)$',views.TextQuesionView.as_view()),
    url(r'^choicequestion/(?P<pk>\w+)$',views.ChoiceQuestionView.as_view()),
    url(r'^textanswer/(?P<pk>\w+)$', views.TextAnswerView.as_view()),
    url(r'^choiceanswer/(?P<pk>\w+)$', views.ChoiceAnswerView.as_view()),
    url(r'^node/(?P<pk>\w+)$', views.NodeView.as_view()),
    url(r'^homework/(?P<pk>\w+)$', views.HomeworkView.as_view()),
    url(r'^material/(?P<pk>\w+)$', views.MaterialView.as_view()),
    url(r'^textquestion$',views.TextQuestionCreationView.as_view()),
    url(r'^choicequestion$',views.ChoiceQuestionCreationView.as_view()),
    url(r'^textanswer$', views.TextAnswerCreationView.as_view()),
    url(r'^choiceanswer$', views.ChoiceAnswerCreationView.as_view()),
    url(r'^node$', views.NodeCreationView.as_view()),
    url(r'^homework$', views.HomeworkCreationView.as_view()),
    url(r'^material$', views.MaterialCreationView.as_view()),
]