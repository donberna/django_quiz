from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser
from users.models import *

from .serializers import *
from .permissions import hasPermission
# Create your views here.
#-----------------------------------
#	questions 
#-----------------------------------

# vista para crear una pregunta verdadero/falso
class True_False_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new True_False question 
	  """
	  serializer_class = TF_Question_Serializer
	  permission_classes = (hasPermission, )


# vista para listar todas las preguntas verdadero/falso
class True_False_List_View(generics.ListAPIView):
	  """
	  A simple View to show all True_False questions
	  """
	  serializer_class = TF_Retireve_Question_Serializer
	  queryset = TF_Question.objects.all()
	  permission_classes = (hasPermission, )


# vista para actualizar una pregunta verdadero/falso
class True_False_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all True_False questions
      """
      serializer_class = TF_Question_Serializer
      queryset = TF_Question.objects.all()
      permission_classes = (hasPermission,)


# vista para crear una pregunta de opcion multiple
class Multichoice_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Multichoice question.
	  """
	  serializer_class = Multichoice_Serializer
	  permission_classes = (hasPermission,)


# vista para listar todas las preguntas de opcion multiple
class Multichoice_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Multichoice questions
	  """
	  serializer_class = MC_Retireve_Question_Serializer
	  queryset = MCQuestion.objects.all()
	  permission_classes = (hasPermission,)


# vista para actualizar una pregunta de opcion multiple 
class Multichoice_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = MC_Retireve_Question_Serializer
      queryset = MCQuestion.objects.all()
      permission_classes = (hasPermission, )


# vista para crear una respuesta de preguntas de opcion multiple (me parece que nada la esta usando)
class Multichoice_Answer_Create(generics.CreateAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Answer_MC_Question_Serializer
      permission_classes = (hasPermission,)


# vista para crear varias respuestas de preguntas de opcion multiple
import json
class Multichoice_Answer_Create_multiple(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (hasPermission,)
  
    def post(self, request, format=None):
        #print("recibo algo")

        id_q = request.POST.get('id_ask')
        question = MCQuestion.objects.get(id=id_q)
        number = int(request.POST.get('number'))
        diccionario = request.POST.dict() 

        if number!= 0 :
          
          for index in range(number):
            string = str(index)
            content = diccionario[string+'[content]']
            correct = diccionario[string+'[correct]']
            serializer = Answer_MC_Question_Serializer(data = {'question': question, 'content' : content, 'correct' : correct})
            
            if serializer.is_valid():
                serializer.save()
                #print 'creo'
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        return Response({'received data': "ok"})
    

# vista para actualizar varias respuestas de preguntas de opcion multiple
class Multichoice_Answer_Update_multiple(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (hasPermission,)
  
    def post(self, request, format=None):
    
        id_q = request.POST.get('id_ask')
        question = MCQuestion.objects.get(id=id_q)
        number = int(request.POST.get('number'))
        diccionario = request.POST.dict() 
    
        if number!= 0 :

          for index in range(number):
            
            string = str(index)
            id_answer = diccionario[string+'[id]']
            answer = Answer.objects.get(id =id_answer)
            content = diccionario[string+'[content]']
            correct = diccionario[string+'[correct]']
            serializer = Answer_MC_Question_Serializer(answer, data = {'question': question, 'content' : content, 'correct' : correct})
            
            if serializer.is_valid():
                serializer.save()
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        return Response({'received data': "ok"})


# vista para listar todas las opciones de respuesta de una pregunta de opcion multiple
class Multichoice_Answer_List_View(generics.ListAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Answer_MC_Question_Serializer
      permission_classes = (hasPermission, )

      def get_queryset(self):
        queryset = Answer.objects.all();
        return queryset.filter(question=self.kwargs['pk'])


# vista para ver una opcion de respuesta multiopcion en especifico 
class Multichoice_Answer_Detail(generics.ListAPIView):
      """
      A simple View to show all Multichoice questions
      """
      serializer_class = Multichoice_Serializer
      permission_classes = (hasPermission,)

      def get_queryset(self):
        queryset = Answer.objects.all();
        return queryset.filter(question=self.kwargs['pk'])



# vista para crear una pregunta abierta
class Essay_Create_View(generics.CreateAPIView):
	  """
	  A simple View to create a new Essay question.
	  """
	  serializer_class = E_Question_Serializer
	  permission_classes = (hasPermission,)


# vista para listar todas las preguntas abiertas
class Essay_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Essay questions
	  """
	  serializer_class = E_Retireve_Question_Serializer
	  queryset = Essay_Question.objects.all()
	  permission_classes = (hasPermission,)


# vista para actualizar una pregunta abierta
class Essay_Update_View(viewsets.ModelViewSet):
      """
      A simple View to show all Essay questions
      """
      serializer_class = E_Retireve_Question_Serializer
      queryset = Essay_Question.objects.all()
      permission_classes = (hasPermission,)


# vista para traer una pregunta dependiendo del tipo de pregunta que se pida 
class Question_Detail_View(APIView):
    """
    View to bring the info of a quesion
    """
    permission_classes = (IsAuthenticated, )
    
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
"""
class Category_Create_View(generics.CreateAPIView):
	  
	  A simple View to create a new Category.
    
	  serializer_class = Category_Serializer
	  permission_classes = (AllowAny,)


class Category_List_View(generics.ListAPIView):
	  
	  A simple View to show all Category
	  
	  serializer_class = Category_Serializer
	  queryset = Category.objects.all()
	  permission_classes = (AllowAny,)
    



class Category_Update_View(viewsets.ModelViewSet):
      
      A simple View to show all Category
      
      serializer_class = Category_Serializer
      queryset = Category.objects.all()
      permission_classes = (AllowAny,)




class Subcategory_Create_View(generics.CreateAPIView):
	  
	  A simple View to create a new SubCategory.
    
	  serializer_class = Subcategory_Serializer
	  permission_classes = (AllowAny,)



class Subcategory_List_View(generics.ListAPIView):
	  
	  A simple View to show all SubCategory
    
	  serializer_class = Subcategory_Retrieve_Serializer
	  queryset = SubCategory.objects.all()
	  permission_classes = (AllowAny,)



class SubCategory_Update_View(viewsets.ModelViewSet):
      
      A simple View to show all Category
      
      serializer_class = Subcategory_Retrieve_Serializer
      queryset = SubCategory.objects.all()
      permission_classes = (AllowAny,)
"""


#-----------------------------------
#	Quiz
#-----------------------------------

#Vista para crear un quiz
class Quiz_Create_View(generics.CreateAPIView):
  """
	A simple View to create a new Quiz.
	"""
  serializer_class = Quiz_Serializer
  permission_classes = (hasPermission,)


#Vista para listar todos los quices creados 
class Quiz_List_View(generics.ListAPIView):
	  """
	  A simple View to show all Quiz
	  """
	  serializer_class = Quiz_Retrieve_Serializer
	  permission_classes = (IsAuthenticated, )

	  def get_queryset(self):
	  	queryset = Quiz.objects.all();
	  	return queryset.filter(draft=False)


# vista para actualizar un quiz 
class Quiz_Update_View(viewsets.ModelViewSet):
    """
    View to bring the info of a quiz
    """
    queryset = Quiz.objects.all()
    serializer_class = Quiz_Retrieve_Serializer
    permission_classes = (hasPermission,)

    def destroy(self, request, pk, format=None, **kwargs):
        #print 'deletio'
        quiz = self.get_object()
        #print quiz
        score = Scores.objects.get(id_event=quiz.id)
        #print score

        # Se envia la senal para disminuir los puntos con los que se gana la medalla
        badge = kwargs['slug']

        calculate_points_end_badge.send(sender=Quiz_Retrieve_Serializer,author=request.user, badge=badge, points=score.score, action='remove', element='quiz', instance_element=quiz)

        
        # se borra el puntaje y el quiz 
        score.delete()
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# vista para traer un quiz dependiendo de la catgoria (esta vista no esta funcionando)
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
# sitting = progreso del usuario en el quiz 
#-----------------------------------

# vista para traer todos los sittings creados 
class Quiz_Sitting_View(generics.ListAPIView):
    queryset = Sitting.objects.all()
    serializer_class = Sitting_Serializer
    
    permission_classes = (IsAuthenticated, )


from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# vista para crear una sitting en el momento de tomar un quiz 
class Quiz_Create_Sitting_View(APIView):
    
    permission_classes = (IsAuthenticated, )

    def dispatch(self, request, *args, **kwargs):    
        return super(Quiz_Create_Sitting_View, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        # se obtienen el quiz y el usuario 
        quiz = get_object_or_404(Quiz, id=self.kwargs['pk_quiz'])
        logged_in_user = User.objects.get(pk= request.POST['id'])

        # se llama a la funcion del modelo donde 
        # 1. busca el sitting por usuario y quiz 
        #   1.1 si existe lo retorna, y si hay varios retorna el que no esta terminado
        # 2. Si no encuentra un sitting asosiado lo crea 

        sitting = Sitting.objects.user_sitting(logged_in_user, quiz)
        serializer = Sitting_Serializer(sitting)
        return  Response(serializer.data)
        

# vista para actualizar un sitting 
class Quiz_update_sitting_View(viewsets.ModelViewSet):
    queryset = Sitting.objects.all()
    serializer_class = Sitting_Serializer
    permission_classes = (IsAuthenticated, )


#Vista pa calificar una pregunta en el momento que se hacen los quices
# las preguntas essay por defecto quedan incorrectas 
from django.contrib.contenttypes.models import ContentType
class Quiz_Qualify_View(APIView):

    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        #print 'post'
        id = request.POST['id']
        clase = request.POST['clase']
        answered = request.POST['answered']
        correcta = ""
        mc_answer = ""
        
        if clase == str(ContentType.objects.get_for_model(TF_Question)):
            #print 'TF_Question'
            question = TF_Question.objects.get(id = id)
            serializer = TF_Retireve_Question_Serializer(question)
            correcta = question.check_if_correct(answered)

        if clase == str(ContentType.objects.get_for_model(MCQuestion)):
            #print 'MC_Question'
            question = MCQuestion.objects.get(id = id)
            serializer= MC_Retireve_Question_Serializer(question)
            correcta = question.check_if_correct(answered)
            mc_answer = question.answer_choice_to_string(answered)
            

            
        if clase == str(ContentType.objects.get_for_model(Essay_Question)):
            #print 'E_Question'
            question = Essay_Question.objects.get(id = id)
            serializer= E_Retireve_Question_Serializer(question)
            #print question.check_if_correct(answered)
            correcta = question.check_if_correct(answered)
            #correcta = False

        #print correcta
        data = serializer.data
        data.update({'answerMC': mc_answer})
        data.update({'correcta': correcta})
        data.update({'answered': answered})

        return Response(data)


#-----------------------------------
#	finish Quiz 
#-----------------------------------
# no se para que era esto lo tenia la app 
class Quiz_Marker_Mixin(object):
    def dispatch(self, *args, **kwargs):
        return super(Quiz_Marker_Mixin, self).dispatch(*args, **kwargs)


# vista para traer un quiz por su titulo (Esto no esta funcionando) 
class Sitting_Filter_Title_Mixin(object):
    def get_queryset(self):
        queryset = super(Sitting_Filter_Title_Mixin, self).get_queryset()
        quiz_filter = self.request.GET.get('quiz_filter')
        if quiz_filter:
            queryset = queryset.filter(quiz__title__icontains=quiz_filter)

        return queryset


#vista para traer la lista de quizes completos de todos los usuarios 
class Quiz_Marking_List_View(Quiz_Marker_Mixin, Sitting_Filter_Title_Mixin, generics.ListAPIView):
    serializer_class = Sitting_retrieve_Serializer
    
    permission_classes = (hasPermission,)

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


# vista para calificar una pregunta abierta por parte del docente 
class Quiz_Sitting_Change_Qualify(APIView):
    
    permission_classes = (hasPermission, )

    def post(self,request):
      #print 'post'
  
      id_sitting = request.POST.get('id_sitting')
      id_question = request.POST.get('id_question', None)
      

      sitting = Sitting.objects.get( id = id_sitting)
      if id_question:
        #print 'if id_question'
        question = Question.objects.get_subclass(id=int(id_question))
        if int(id_question) in sitting.get_incorrect_questions:
          #print 'if remove'
          sitting.remove_incorrect_question(question)

      serializer = Sitting_Serializer(sitting)
      serializer2 = Sitting_Serializer(sitting, data = serializer.data)     
      if serializer2.is_valid():
        serializer2.save()

        #print 'Actualizo'
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
      return Response({'msj': "Sitting actualizado"})

  

# vista para traer el detalle de un quiz terminado 
class Quiz_Marking_Detail_View(Quiz_Marker_Mixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = Sitting_retrieve_Serializer
    
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Sitting.objects.filter(id = self.kwargs['pk'])


# vista para traer el supuesto progreso de un usuario frente a los quices (Esto no esta funcionando)
class Quiz_User_Progress_View(generics.ListAPIView):
    queryset = Progress.objects.all()
    serializer_class = Progress_Serializer
    
    permission_classes = (AllowAny,)

    def dispatch(self, request, *args, **kwargs):
    	#print 'dispatch'
        return super(Quiz_User_Progress_View, self)\
            .dispatch(request, *args, **kwargs)


#vista para traer todos los intentos de los quizzes de un usuario
class Quiz_show_exams_View(generics.ListAPIView):
    serializer_class = Sitting_Serializer #
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        #print self.kwargs['pk']
        user = self.kwargs['pk']
        return Sitting.objects.filter(user=user, complete=True)

