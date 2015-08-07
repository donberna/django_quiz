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
	  serializer_class = Create_MC_Question_Serializer
	  permission_classes = (AllowAny,)


class Multichoice_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Multichoice questions
	  """
	  serializer_class = List_Multichoice_Serializer
	  queryset = MCQuestion.objects.all()
	  permission_classes = (AllowAny,)


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


class Quiz_Marking_List_View(Quiz_Marker_Mixin, Sitting_Filter_Title_Mixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Sitting_Serializer

    def get_queryset(self):
        
        queryset = Sitting.objects.filter(complete=True)

        """
        Aqui se acomoda lo de filtrar por el usuario 

        user_filter = self.request.GET.get('user_filter')
        if user_filter:
            queryset = queryset.filter(user__username__icontains=user_filter)
        """
        return queryset


class Quiz_Marking_Detail_View(Quiz_Marker_Mixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = Sitting_Serializer

    def get_queryset(self):
        return Sitting.objects.filter(id = self.kwargs['pk'])

    # si va a cambiar el valor respuesta por 
    def post(self, request, *args, **kwargs):
        sitting = self.get_object()

        q_to_toggle = request.POST.get('qid', None)
        if q_to_toggle:
            q = Question.objects.get_subclass(id=int(q_to_toggle))
            if int(q_to_toggle) in sitting.get_incorrect_questions:
                sitting.remove_incorrect_question(q)
            else:
                sitting.add_incorrect_question(q)

        return self.get(request)

"""
	esto  retorna un diccionario representando el contexto del template no se como acomodarlo en rest 
	Segun lo q he buscado en el seriaizar con  to_representation aunque no estoy seguro

    def get_context_data(self, **kwargs):
    	print 'context'
        context = super(Quiz_Marking_Detail_View, self).get_context_data(**kwargs)
        context['questions'] =\
            context['sitting'].get_questions(with_answers=True)
        print context
        return context
"""



class Quiz_User_Progress_View(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Progress.objects.all()
    serializer_class = Progress_Serializer

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
    	print 'dispatch'
        return super(Quiz_User_Progress_View, self)\
            .dispatch(request, *args, **kwargs)

"""
	Falta acomodar esto que es para traer todos los intentos de los quizzes
    def get_context_data(self, **kwargs):
    	print 'get_context_data'
        context = super(Quiz_User_Progress_View, self).get_context_data(**kwargs)
        progress, c = Progress.objects.get_or_create(user=self.request.user)
        context['cat_scores'] = progress.list_all_cat_scores
        context['exams'] = progress.show_exams()
        return context
"""








