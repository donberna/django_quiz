from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework import serializers
from quiz.models import Question
from true_false.models import TF_Question
from multichoice.models import MCQuestion, Answer
from essay.models import Essay_Question
from quiz.models import Category, SubCategory, Sitting, Progress, Quiz
from django.contrib.contenttypes.models import ContentType
import json

#-----------------------------------
#   questions 
#-----------------------------------

class TF_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    class Meta():
        model = TF_Question


class TF_Retireve_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    clase = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        if obj.category == None:
            return ""
        else:
            return {'id':obj.category.id,'nombre':str(obj.category.category)}    

    def get_sub_category(self, obj):
        if obj.sub_category ==None:
            return ""
        else: 
            return {'id':obj.sub_category.id,'nombre':str(obj.sub_category.sub_category)}    
    
    def get_clase(self, obj):
        tipo = str(ContentType.objects.get_for_model(TF_Question))
        return tipo

    class Meta():
        model = TF_Question
        fields = ( 'id', 'content', 'category', 'sub_category', 'figure', 'quiz', 'explanation', 'correct', 'clase')
        read_only_fields = ('id', 'clase')


class Answer_MC_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Asks
    """
    
    class Meta():
        model = Answer
        fields = ( 'id', 'question', 'content', 'correct')


class Multichoice_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to list TF_Question
    """
    class Meta():
        model = MCQuestion


class MC_Retireve_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    clase = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    
    def get_answers(self, obj):
        print 'anwers'
        objectQuerySet = Answer.objects.filter(question = obj.id)
        if len(objectQuerySet) == 0:
            return '{}'
        else:
            data = []
            for item in objectQuerySet:
                data.append("{ 'id':"+str(item.id)+", 'question':"+str(item.question.id)+", 'content':"+item.content+", 'correct':"+str(item.correct)+"}")
            return data
    
    def get_category(self, obj):
        if obj.category == None:
            return ""
        else:
            return {'id':obj.category.id,'nombre':str(obj.category.category)}    

    def get_sub_category(self, obj):
        if obj.sub_category ==None:
            return ""
        else: 
            return {'id':obj.sub_category.id,'nombre':str(obj.sub_category.sub_category)}    
    
    def get_clase(self, obj):
        tipo = str(ContentType.objects.get_for_model(MCQuestion))
        return tipo

    class Meta():
        model = MCQuestion
        fields = ( 'id', 'content', 'category', 'sub_category', 'figure', 'quiz', 'explanation', 'answer_order', 'clase', 'answers')
        read_only_fields = ('id', 'clase')


class E_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Essay_Question
    """
    class Meta():
        model = Essay_Question


class E_Retireve_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    clase = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()


    def get_category(self, obj):
        if obj.category == None:
            return ""
        else:
            return {'id':obj.category.id,'nombre':str(obj.category.category)}        

    def get_sub_category(self, obj):
        if obj.sub_category ==None:
            return ""
        else: 
            return {'id':obj.sub_category.id,'nombre':str(obj.sub_category.sub_category)}    
    
    def get_clase(self, obj):
        tipo = str(ContentType.objects.get_for_model(Essay_Question))
        return tipo#   

    class Meta():
        model = Essay_Question
        fields = ( 'id', 'content', 'category', 'sub_category', 'figure', 'quiz', 'explanation', 'clase')
        read_only_fields = ('id', 'clase')


#-----------------------------------
#   Category and Subcategory 
#-----------------------------------

class Category_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to list TF_Question
    """
    class Meta():
        model = Category


class Subcategory_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create SubCategory
    """
    class Meta():
        model = SubCategory


class Subcategory_Retrieve_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to retrieve SubCategory
    """
    category = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        if obj.category == None:
            return ""
        else:
            return {'id':obj.category.id,'nombre':str(obj.category.category)}        

    class Meta():
        model = SubCategory

#-----------------------------------
#   Quiz
#-----------------------------------

class Quiz_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    
    class Meta():
        model = Quiz
        fields = ('id' ,'title', 'description', 'url', 'category', 'random_order', 'max_questions', 'answers_at_end', 'exam_paper', 'single_attempt', 'pass_mark', 'success_text', 'fail_text', 'draft', 'get_max_score', 'quiz')
        read_only_fields = ('id')


class Quiz_Retrieve_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """

    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        if obj.category == None:
            return ""
        else:
            return {'id':obj.category.id,'nombre':str(obj.category.category)}    

    class Meta():
        model = Quiz
        fields = ('id' ,'title', 'description', 'url', 'category', 'random_order', 'max_questions', 'answers_at_end', 'exam_paper', 'single_attempt', 'pass_mark', 'success_text', 'fail_text', 'draft', 'get_max_score', 'quiz')
        read_only_fields = ('id')


#-----------------------------------
#   take Quiz 
#-----------------------------------
    


#-----------------------------------
#   finish Quiz 
#-----------------------------------
class Sitting_retrieve_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    quiz = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return  obj.user.get_full_name()


    def get_quiz(self, obj):
        return obj.quiz.title

    class Meta():
        model = Sitting
        fields = ('id', 'user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end', 'get_percent_correct', 'check_if_passed', 'result_message', 'questions_with_user_answers', 'get_max_score')
        read_only_fields = ('id')



class Sitting_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """    
    class Meta():
        model = Sitting
        fields = ('id', 'user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end')
        read_only_fields = ('id')

class Progress_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    class Meta():
        model = Progress
        fields = ('id', 'user', 'score', 'list_all_cat_scores')