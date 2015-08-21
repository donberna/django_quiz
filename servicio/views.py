from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
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
	  serializer_class = Multichoice_Serializer
	  queryset = MCQuestion.objects.all()
	  permission_classes = (AllowAny,)


class Multichoice_Answer_Create(generics.CreateAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Answer_MC_Question_Serializer
      permission_classes = (AllowAny,)


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
	  serializer_class = E_Question_Serializer
	  queryset = Essay_Question.objects.all()
	  permission_classes = (AllowAny,)


class Question_Detail_View(APIView):
    """
    View to bring the info of a quiz
    """
    permission_classes = (AllowAny,)
    
    def get(self,*args, **kwargs):
        queryset = Question.objects.get_subclass(id = self.kwargs['pk'])
        print queryset
        clase = queryset.__class__
        
        if clase is Essay_Question:
            serializer = E_Question_Serializer(queryset)
        
        #if clase is MCQuestion:
            #serializer= Create_MC_Question_Serializer(queryset)
        
        if clase is TF_Question:
            serializer = TF_Question_Serializer(queryset)

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
	  serializer_class = Subcategory_Serializer
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
	  serializer_class = Quiz_Serializer
	  permission_classes = (AllowAny,)

	  def get_queryset(self):
	  	queryset = Quiz.objects.all();
	  	return queryset.filter(draft=False)


class Quiz_Detail_View(viewsets.ReadOnlyModelViewSet):
    """
    View to bring the info of a quiz
    """
    permission_classes = (AllowAny,)
    queryset = Quiz.objects.all()
    serializer_class = Quiz_Serializer


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

class Quiz_Take_View(APIView):
    
    permission_classes = (AllowAny,)

    def dispatch(self, request, *args, **kwargs):
        
        #se obtiene el quiz 
        quiz = get_object_or_404(Quiz, id=self.kwargs['pk_quiz'])
        id_quiz = quiz.id
        #print id_quiz

        #se pregunta si el usuario esta autenticado  
        logged_in_user = self.request.user
        print 'logged_in_user'
        print logged_in_user

        # se ontienen las preguntas del quiz 
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
                    'user_answers':'{}'}

        #print sitting

        return super(Quiz_Take_View, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = Sitting_Serializer(data=self.sitting)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




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
    serializer_class = Sitting_Serializer

    def get_queryset(self):    
        queryset = Sitting.objects.filter(complete=True)

    #    """
    #    Aqui se acomoda lo de filtrar por el usuario 

    #    user_filter = self.request.GET.get('user_filter')
    #    if user_filter:
    #        queryset = queryset.filter(user__username__icontains=user_filter)
    #    """
    #    return queryset


class Quiz_Marking_Detail_View(Quiz_Marker_Mixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = Sitting_Serializer

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

