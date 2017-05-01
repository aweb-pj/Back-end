from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.exceptions import PermissionDenied
from Tree.serializers import *
import os
import json

# Create your views here.


class TextQuesionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TextQuestionSerializer
    queryset = TextQuestion.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveUpdateDestroyAPIView, self).initial(request, *args, **kwargs)


class ChoiceQuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceQuestionSerializer
    queryset = ChoiceQuestion.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveUpdateDestroyAPIView, self).initial(request, *args, **kwargs)


class TextAnswerView(generics.RetrieveAPIView):
    serializer_class = TextAnswerSerializer
    queryset = TextAnswer.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveAPIView, self).initial(request, *args, **kwargs)


class ChoiceAnswerView(generics.RetrieveAPIView):
    serializer_class = ChoiceAnswerSerializer
    queryset = ChoiceAnswer.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveAPIView, self).initial(request, *args, **kwargs)


class MaterialView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveUpdateDestroyAPIView, self).initial(request, *args, **kwargs)


class HomeworkView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveUpdateDestroyAPIView, self).initial(request, *args, **kwargs)


class NodeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['GET','PUT','DELETE']
        authentication_dict['teacher'] = ['GET', 'PUT', 'DELETE']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.RetrieveUpdateDestroyAPIView, self).initial(request, *args, **kwargs)


class TextQuestionCreationView(generics.CreateAPIView):
    serializer_class = TextQuestionSerializer
    queryset = TextQuestion.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class ChoiceQuestionCreationView(generics.CreateAPIView):
    serializer_class = ChoiceQuestionSerializer
    queryset = ChoiceQuestion.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class TextAnswerCreationView(generics.CreateAPIView):
    serializer_class = TextAnswerSerializer
    queryset = TextAnswer.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class ChoiceAnswerCreationView(generics.CreateAPIView):
    serializer_class = ChoiceAnswerSerializer
    queryset = ChoiceAnswer.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class MaterialCreationView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class HomeworkCreationView(generics.CreateAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


class NodeCreationView(generics.CreateAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

    def initial(self, request, *args, **kwargs):
        authentication_dict = {}
        authentication_dict['student'] = ['POST']
        authentication_dict['teacher'] = ['POST']
        if 'role' not in request.session:
            raise PermissionDenied("not logged in")
        if request.method not in authentication_dict[request.session['role']]:
            raise PermissionDenied("not allowed")
        super(generics.CreateAPIView, self).initial(request, *args, **kwargs)


# class TextQuestionView(generics.GenericAPIView):
#     serializer_class = TextQuestionSerializer
#     queryset = TextQuestion.objects.all()
#
#     def get_object(self,pk):
#         result = self.queryset.filter(pk=pk)
#         if result.exists():
#             return result[0]
#         else:
#             return None
#
#     def get(self,request,pk):
#         question = self.queryset.filter(pk=pk)
#         if question.exists():
#             serializer = TextQuestionSerializer(question[0])
#             return Response(data = serializer.data,status = status.HTTP_200_OK)
#         else:
#             return Response(status = status.HTTP_404_NOT_FOUND)
#
#     def put(self,request,pk):
#         input_data = request.data
#         question = self.get_object(pk)
#         serializer = TextQuestionSerializer(instance=question,data = input_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status = status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_question(request,type):
    input_data = request.data
    if type == "text":
        serializer = TextQuestionSerializer(data=input_data)
    elif type == "choice":
        serializer = ChoiceQuestionSerializer(data=input_data)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def student_login(request):
    input_data = request.data
    login_id = input_data['id']
    login_password = input_data['password']
    student = Student.objects.all().filter(student_id=login_id)
    login_result = {'result':None}
    if student.exists():
        student = student[0]
        if student.student_password == login_password:
            request.session['role'] = 'student'
            request.session['id'] = student.student_id
            login_result['result'] = 'success'
            return Response(data=login_result,status=status.HTTP_200_OK)
        else:
            login_result['result'] = 'failure'
            return Response(data=login_result,status=status.HTTP_404_NOT_FOUND)
    else:
        login_result['result'] = 'failure'
        return Response(data=login_result,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def teacher_login(request):
    input_data = request.data
    login_id = input_data['id']
    login_password = input_data['password']
    teacher = Teacher.objects.all().filter(teacher_id=login_id)
    login_result = {'result':None}
    if teacher.exists():
        teacher = teacher[0]
        if teacher.teacher_password == login_password:
            request.session['role'] = 'teacher'
            request.session['id'] = teacher.teacher_id
            login_result['result'] = 'success'
            return Response(data=login_result,status=status.HTTP_200_OK)
        else:
            login_result['result'] = 'failure'
            return Response(data=login_result,status=status.HTTP_404_NOT_FOUND)
    else:
        login_result['result'] = 'failure'
        return Response(data=login_result,status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def logout(request):
    try:
        del request.session['id']
        del request.session['role']
    except KeyError:
        pass
    return Response({'logout':'true'},status=status.HTTP_200_OK)


def load_tree_teacher(node):
    result_data = NodeSerializer(instance=node).data
    result_data['children'] = []
    for child in node.get_children():
        result_data['children'].append(load_tree_teacher(child))
    return result_data


def load_tree_student(node,student_id):
    result_data = NodeSerializer(instance=node).data
    result_data['children'] = []
    homework = result_data['homework']
    if len(homework) == 1:
        homework = homework[0]
        for choice_question in homework['choice_questions']:
            current_question = ChoiceQuestion.objects.filter(pk=choice_question['pk'])[0]
            current_student = Student.objects.filter(student_id=student_id)
            answer = ChoiceAnswer.objects.filter(question=current_question).filter(student=current_student)
            if answer.exists():
                answer = answer[0]
                choice_question['answer'] = answer.answer
            else:
                choice_question['answer'] = None
        for text_question in homework['text_questions']:
            current_question = TextQuestion.objects.filter(pk=text_question['pk'])[0]
            current_student = Student.objects.filter(student_id=student_id)
            answer = TextAnswer.objects.filter(question=current_question).filter(student=current_student)
            if answer.exists():
                answer = answer[0]
                text_question['answer'] = answer.answer
            else:
                text_question['answer'] = None

    for child in node.get_children():
        result_data['children'].append(load_tree_student(child,student_id))
    return result_data


@api_view(['GET'])
def get_tree(request):
    if 'role' not in request.session:
        raise PermissionDenied("login first")
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'root.json')
    with open(file_path, "r") as f:
        root_json = json.load(f)
        root_pk = root_json['pk']
        root_node = Node.objects.filter(pk=root_pk)[0]
        role = request.session['role']
        json_result = None
        if role == 'teacher':
            json_result = load_tree_teacher(root_node)
        elif role == 'student':
            json_result = load_tree_student(root_node, request.session['id'])
        else:
            raise PermissionDenied("not logged in")
        return Response(data=json_result,status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request,role):
    input_data = request.data
    if role == 'student':
        serializer = StudentSerializer(data=input_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data,status=status.HTTP_201_CREATED)
        else:
            return Response(data={"error_message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    elif role == 'teacher':
        serializer = TeacherSerializer(data=input_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data,status=status.HTTP_201_CREATED)
        else:
            return Response(data={"error_message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"error_message":"wrong role"},status=status.HTTP_400_BAD_REQUEST)
