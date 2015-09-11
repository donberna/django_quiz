from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser

from .serializers import *

# Create your views here.
#-----------------------------------
#	questions 
#-----------------------------------

class True_False_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new True_False question 
	  """
	  serializer_class = TF_Question_Serializer
	  permission_classes = (AllowAny,)


class True_False_List_View(generics.ListAPIView):
	  """
	  A simple View to show all True_False questions
	  """
	  serializer_class = TF_Retireve_Question_Serializer
	  queryset = TF_Question.objects.all()
	  permission_classes = (AllowAny,)


class True_False_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all True_False questions
      """
      serializer_class = TF_Question_Serializer
      queryset = TF_Question.objects.all()
      permission_classes = (AllowAny,)



class Multichoice_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Multichoice question.
	  """
	  serializer_class = Multichoice_Serializer
	  permission_classes = (AllowAny,)


class Multichoice_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Multichoice questions
	  """
	  serializer_class = MC_Retireve_Question_Serializer
	  queryset = MCQuestion.objects.all()
	  permission_classes = (AllowAny,)


class Multichoice_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = MC_Retireve_Question_Serializer
      queryset = MCQuestion.objects.all()
      permission_classes = (AllowAny,)


class Multichoice_Answer_Create(generics.CreateAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Answer_MC_Question_Serializer
      permission_classes = (AllowAny,)


import json
class Multichoice_Answer_Create_multiple(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)
  
    def post(self, request, format=None):
        print("recibo algo")
        print request.POST
        #print request.POST.get('_content')
        #answers = json.loads(request.POST.get('_content'))
        
        id_q = request.POST.get('id_ask')
        #id_q =  answers[0]
        #id_q = id_q['id_ask']
        print id_q
        question = MCQuestion.objects.get(id=id_q)

        number = int(request.POST.get('number'))


        print number
        #print answers['contenido[]']
        #print answers[0]
        #print answers['items']
        #print request.POST.get('items')
        diccionario = request.POST.dict() 
        print request.POST.dict()
        if number!= 0 :
          pass
          for index in range(number):
            #print index
            string = str(index)
            #print diccionario[string+'[content]']
            content = diccionario[string+'[content]']
            #print content
            correct = diccionario[string+'[correct]']
            #print correct
            serializer = Answer_MC_Question_Serializer(data = {'question': question, 'content' : content, 'correct' : correct})
            if serializer.is_valid():
                serializer.save()
                print 'creo'
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        return Response({'received data': "ok"})
    

class Multichoice_Answer_Update_multiple(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)
  
    def post(self, request, format=None):
        print("recibo algo")
        print request.POST
        #print request.POST.get('_content')
        #answers = json.loads(request.POST.get('_content'))
        
        id_q = request.POST.get('id_ask')
        #id_q =  answers[0]
        #id_q = id_q['id_ask']
        print id_q
        question = MCQuestion.objects.get(id=id_q)

        number = int(request.POST.get('number'))


        print number
        #print answers['contenido[]']
        #print answers[0]
        #print answers['items']
        #print request.POST.get('items')
        diccionario = request.POST.dict() 
        print request.POST.dict()
        if number!= 0 :
          pass
          for index in range(number):
            #print index
            string = str(index)
            #print diccionario[string+'[content]']
            id_answer = diccionario[string+'[id]']
            answer = Answer.objects.get(id =id_answer)
            print answer
            #print id_answer
            content = diccionario[string+'[content]']
            #print content
            correct = diccionario[string+'[correct]']
            #print correct
            serializer = Answer_MC_Question_Serializer(answer, data = {'question': question, 'content' : content, 'correct' : correct})
            if serializer.is_valid():
                serializer.save()
                print 'Actualizo'
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        return Response({'received data': "ok"})


class Multichoice_Answer_List_View(generics.ListAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Answer_MC_Question_Serializer
      permission_classes = (AllowAny,)

      def get_queryset(self):
        queryset = Answer.objects.all();
        return queryset.filter(question=self.kwargs['pk'])


class Multichoice_Answer_Detail(generics.ListAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Multichoice_Serializer
      permission_classes = (AllowAny,)

      def get_queryset(self):
        queryset = Answer.objects.all();
        return queryset.filter(question=self.kwargs['pk'])


class Essay_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Essay question.
	  """
	  serializer_class = E_Question_Serializer
	  permission_classes = (AllowAny,)


class Essay_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Essay questions
	  """
	  serializer_class = E_Retireve_Question_Serializer
	  queryset = Essay_Question.objects.all()
	  permission_classes = (AllowAny,)


class Essay_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Essay questions
      """
      serializer_class = E_Retireve_Question_Serializer
      queryset = Essay_Question.objects.all()
      permission_classes = (AllowAny,)


class Question_Detail_View(APIView):
    """
    View to bring the info of a quiz
    """
    permission_classes = (AllowAny,)
    
    def get(self,*args, **kwargs):
        queryset = Question.objects.get_subclass(id = self.kwargs['pk'])
        clase = ContentType.objects.get_for_model(queryset)
        
        if clase is ContentType.objects.get_for_model(Essay_Question):
            serializer = E_Retireve_Question_Serializer(queryset)
        
        if clase is ContentType.objects.get_for_model(MCQuestion):
            serializer = MC_Retireve_Question_Serializer(queryset)
        
        if clase is ContentType.objects.get_for_model(TF_Question):
            serializer = TF_Retireve_Question_Serializer(queryset)
            
        return Response(serializer.data)
        


#-----------------------------------
#	Category and Subcategory 
#-----------------------------------

class Category_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Category.
	  """
	  serializer_class = Category_Serializer
	  permission_classes = (AllowAny,)


class Category_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Category
	  """
	  serializer_class = Category_Serializer
	  queryset = Category.objects.all()
	  permission_classes = (AllowAny,)



class Category_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Category
      """
      serializer_class = Category_Serializer
      queryset = Category.objects.all()
      permission_classes = (AllowAny,)



class Subcategory_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new SubCategory.
	  """
	  serializer_class = Subcategory_Serializer
	  permission_classes = (AllowAny,)


class Subcategory_List_View(generics.ListAPIView):
	  """
	  A simple View to show all SubCategory
	  """
	  serializer_class = Subcategory_Retrieve_Serializer
	  queryset = SubCategory.objects.all()
	  permission_classes = (AllowAny,)


class SubCategory_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Category
      """
      serializer_class = Subcategory_Retrieve_Serializer
      queryset = SubCategory.objects.all()
      permission_classes = (AllowAny,)


#-----------------------------------
#	Quiz
#-----------------------------------

class Quiz_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Quiz.
	  """
	  serializer_class = Quiz_Serializer
	  permission_classes = (AllowAny,)


class Quiz_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Quiz
	  """
	  serializer_class = Quiz_Retrieve_Serializer
	  permission_classes = (AllowAny,)

	  def get_queryset(self):
	  	queryset = Quiz.objects.all();
	  	return queryset.filter(draft=False)


class Quiz_Update_View(viewsets.ModelViewSet):
    """
    View to bring the info of a quiz
    """
    permission_classes = (AllowAny,)
    queryset = Quiz.objects.all()
    serializer_class = Quiz_Retrieve_Serializer


from django.shortcuts import get_object_or_404
class Quiz_List_by_Category_View(generics.ListAPIView):
    """
    View to list the quizzes in a category
    """
    permission_classes = (AllowAny,)
    serializer_class = Quiz_Serializer
 
    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(
            Category,
            category=self.kwargs['category_name']
        )

        return super(Quiz_List_by_Category_View, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Quiz_List_by_Category_View, self)\
            .get_context_data(**kwargs)

        context['category'] = self.category
        return context

    def get_queryset(self):
        queryset = Quiz.objects.all();
        return queryset.filter(category=self.category, draft=False)


#-----------------------------------
#	take Quiz 
#-----------------------------------

class Quiz_Sitting_View(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Sitting.objects.all()
    serializer_class = Sitting_Serializer


from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

class Quiz_Create_Sitting_View(APIView):
    
    permission_classes = (AllowAny,)

    def dispatch(self, request, *args, **kwargs):    
        return super(Quiz_Create_Sitting_View, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        # se obtienen el quiz y el usuario 
        quiz = get_object_or_404(Quiz, id=self.kwargs['pk_quiz'])
        #id_quiz = quiz.id

        logged_in_user = request.POST['id']
        print logged_in_user

        sitting = Sitting.objects.user_sitting(logged_in_user, quiz)
        return  sitting
        """
        #se busca si ya hay un sitting asosiado a ese usuario con ese quiz 
        #sitting = Sitting.objects.filter(quiz = id_quiz, user = logged_in_user)

        # se obtienen las preguntas del quiz 
        if quiz.random_order is True:
            question_set = Question.objects.filter(quiz= quiz.id).order_by('?')
        else:
            question_set = Question.objects.filter(quiz= quiz.id)

        question_set = question_set.values_list('id', flat=True)
        if quiz.max_questions and quiz.max_questions < len(question_set):
            question_set = question_set[: quiz.max_questions]

        questions = ",".join(map(str, question_set)) + ","
        #print questions

        #1 crear el sitting con lo q ya tengo 
        self.sitting = { 'user':logged_in_user,
                    'quiz':id_quiz,
                    'question_order':questions,
                    'question_list':questions,
                    'incorrect_questions':"",
                    'current_score':0,
                    'complete':False,
                    'user_answers':"{}"}

        serializer = Sitting_Serializer(data=self.sitting)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """
        

class Quiz_update_sitting_View(viewsets.ModelViewSet):
    queryset = Sitting.objects.all()
    serializer_class = Sitting_Serializer
    permission_classes = (AllowAny, )


from django.contrib.contenttypes.models import ContentType
class Quiz_Qualify_View(APIView):

    permission_classes = (AllowAny,)
    
    def post(self,request):
        print 'post'
        print ContentType.objects.get_for_model(MCQuestion)
        id = request.POST['id']
        clase = request.POST['clase']
        answered = request.POST['answered']
        correcta = ""
        mc_answer = ""
        
        if clase == str(ContentType.objects.get_for_model(TF_Question)):
            
            question = TF_Question.objects.get(id = id)
            serializer = TF_Retireve_Question_Serializer(question)

            if str(serializer.data['correct']) == answered:
                correcta = True
            else:
                correcta = False

        if clase == str(ContentType.objects.get_for_model(MCQuestion)):
            print 'MC_Question'
            
            question = MCQuestion.objects.get(id = id)
            serializer= MC_Retireve_Question_Serializer(question)

            answer = Answer.objects.get(id = answered)
            serializer_ans = Answer_MC_Question_Serializer(answer)
            
            mc_answer = serializer_ans.data['content']

            if serializer_ans.data['correct']:
                correcta = True
            else:
                correcta = False

            
        if clase == str(ContentType.objects.get_for_model(Essay_Question)):
            question = Question.objects.get(id = id)
            serializer= E_Retireve_Question_Serializer(question)
            correcta = False

        print correcta
        data = serializer.data
        #data.update({'clase': clase})
        data.update({'answerMC': mc_answer})
        data.update({'correcta': correcta})
        data.update({'answered': answered})

        return Response(data)
        #return Response({'correcta':correcta, 'explanation': serializer.data['explanation']})

#-----------------------------------
#	finish Quiz 
#-----------------------------------

class Quiz_Marker_Mixin(object):
	# no se como acomodar esos decoradores con los permisos
    #@method_decorator(login_required)
    #@method_decorator(permission_required('quiz.view_sittings'))
    def dispatch(self, *args, **kwargs):
        return super(Quiz_Marker_Mixin, self).dispatch(*args, **kwargs)


class Sitting_Filter_Title_Mixin(object):
    def get_queryset(self):
        queryset = super(Sitting_Filter_Title_Mixin, self).get_queryset()
        quiz_filter = self.request.GET.get('quiz_filter')
        if quiz_filter:
            queryset = queryset.filter(quiz__title__icontains=quiz_filter)

        return queryset


#trae la lista de quizes completos de todos los usuarios 
class Quiz_Marking_List_View(Quiz_Marker_Mixin, Sitting_Filter_Title_Mixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Sitting_retrieve_Serializer

    def get_queryset(self):    
        queryset = Sitting.objects.filter(complete=True)
        return queryset

    #    """
    #    Aqui se acomoda lo de filtrar por el usuario 

    #    user_filter = self.request.GET.get('user_filter')
    #    if user_filter:
    #        queryset = queryset.filter(user__username__icontains=user_filter)
    #    """
    #    return queryset


class Quiz_Marking_Detail_View(Quiz_Marker_Mixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = Sitting_retrieve_Serializer

    def get_queryset(self):
        return Sitting.objects.filter(id = self.kwargs['pk'])

    # si va a cambiar el valor respuesta por 
    """def post(self, request, *args, **kwargs):
        sitting = self.get_object()

        q_to_toggle = request.POST.get('qid', None)
        if q_to_toggle:
            q = Question.objects.get_subclass(id=int(q_to_toggle))
            if int(q_to_toggle) in sitting.get_incorrect_questions:
                sitting.remove_incorrect_question(q)
            else:
                sitting.add_incorrect_question(q)

        return self.get(request)"""



class Quiz_User_Progress_View(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Progress.objects.all()
    serializer_class = Progress_Serializer

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
    	print 'dispatch'
        return super(Quiz_User_Progress_View, self)\
            .dispatch(request, *args, **kwargs)


#trae todos los intentos de los quizzes de un usuario
class Quiz_show_exams_View(generics.ListAPIView):
    permission_classes = (AllowAny,)
    #queryset = Progress.objects.all()
    serializer_class = Sitting_Serializer #
    def get_queryset(self):
        print self.kwargs['pk']
        user = self.kwargs['pk']
        return Sitting.objects.filter(user=user, complete=True)

