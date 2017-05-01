# Teacher

{

    teacher_name (char,max 100)
    teacher_id (char,max 100,primary key)
    teacher_password (char,max 100)
}

# Student

{

    student_name (char,max 100)
    student_id (char,max 100, primary key)
    student_password (char,max 100)
}

1. To create a teacher or student: use teacher as example , student is the same<br>
* Request:
url:/tree/register/teacher(student)<br>
request_body:{teacher_id:123456,teacher_name:John,teacher_password:123456}<br>
method = POST<br>
* Response:
if success:<br>
return created object, HTTP 201<br>
if failure:<br>
return example:{error_message:{teacher_id:[teacher with this teacher id already exists.]}} or {error_message:wrong role}, HTTP 400<br>

2. Login: 

* Request:

url:/tree/login/teacher(student)

request_body: {id:123,password:123}

method；POST

* Response:

if success；

{result:success} HTTP 200

if failure:

{result:failure} HTTP 404

3. Logout:

clear out current session

* Request:

url:/tree/logout

request_body:None

method；DELETE

* Response:

{logout:true}

# Node

{

    complete (boolean)
    node_name (char,max 100)
    materials (list of Material)
    homework (list of Homework)
    pk (integer)

}

(get,put,delete)url:/tree/node/pk

(post)url:/tree/node

# Homework

{
    
    homework_name (char,max 100)
    text_questions (list of TextQuestion)
    choice_questions (list of ChoiceQuestion)
    pk (integer)
    node (integer pk of corresponding node)
}

(get,put,delete)url:/tree/homework/pk

(post)url:/tree/homework

# ChoiceQuestion

{

    prompt (char,max 100)
    A (char,max 100)
    B (char,max 100)
    C (char,max 100)
    D (char,max 100)
    pk (integer)
    homework (integer pk for corresponding homework)
    order (integer)
    correct_answer(char, max 100)
}

(get,put,delete)url:/tree/choicequestion/pk

(post)url:/tree/choicequestion

# TextQuestion

{

    prompt (char,max 100)
    pk (integer)
    homework (integer pk for corresponding homework)
    order (integer)
    correct_answer(char, max 100)
}

(get,put,delete)url:/tree/textquestion/pk

(post)url:/tree/textquestion

# TextAnswer

{

    answer (char max 100)
    pk (integer)
    student (integer pk for corresponding student)
    question (integer pk for corresponding question)
}

(get)url:/tree/textanswer/pk

(post)url:/tree/textanswer

# ChoiceAnswer

{

    answer (char max 100)
    pk (integer)
    student (integer pk for corresponding student)
    question (integer pk for corresponding question)
}

(get)url:/tree/choiceanswer/pk

(post)url:/tree/choiceanswer

The api for creating,updating,deleting,getting one of the [Node,Homework,ChoiceQuestion,ChoiceAnswer,
TextQuestion,TextAnswer] is similar:

* PUT->update
* DELETE->delete
* GET->fetch
* POST->create

# Tree
a tree is implemented by traversing from the root node and adding a children attribute(a list of nodes)to each node.Please DONOT delete the root node.

to load the whole tree:

url:/tree/get_tree

method:GET

if the user has not logged in:

HTTP 403 

if the user is a teacher:

just the tree

if the user is a student:

for every question in the tree:

an answer attribute is added, null means no answer yet


# Notice:
1. You need to do the update in a bottom-up approach:
for example if I wish to update a question in a homework, I will use the url for updating a question
and not change the question in the homework and update the homework
2. Answers cannot be updated or deleted(easy to change,should you need to)
3. pk should not be changed and need not be provided in creation
4. when creating a model do remember to add pk for foreign keys
