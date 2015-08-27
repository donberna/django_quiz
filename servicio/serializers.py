from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework import serializers
from quiz.models import Question
from true_false.models import TF_Question
from multichoice.models import MCQuestion, Answer
from essay.models import Essay_Question
from quiz.models import Category, SubCategory, Sitting, Progress, Quiz


#-----------------------------------
#   questions 
#-----------------------------------

class Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    class Meta():
        model = Question


class TF_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    class Meta():
        model = TF_Question


class Answer_MC_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Asks
    """
    
    class Meta():
        model = Answer
        fields = ( 'id', 'question', 'content', 'correct')


"""
class Create_MC_Question_Serializer(serializers.ModelSerializer):
    
    # fields anwers
    answer = Create_Answer_MC_Question_Serializer(many=True)
    #print answer

    def create(self, validated_data):
        answer_content_data = validated_data.pop('content')
        answer_correct_data = validated_data.pop('correct')
        ans = Answer.objects.create(answer_correct_data,answer_content_data)
        mcquestion = MCQuestion.objects.create(answer = ans, **validated_data)        

        return MCQuestion.objects.create(answer = ans, **validated_data)
    #print answer

    class Meta():
        model = MCQuestion
        fields = ( 'id', 'quiz', 'category', 'sub_category', 'figure', 'content', 'explanation', 'objects', 'answer')
        read_only_fields = ('id')
"""


class Multichoice_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to list TF_Question
    """
    class Meta():
        model = MCQuestion


class E_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Essay_Question
    """
    class Meta():
        model = Essay_Question


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


#-----------------------------------
#   take Quiz 
#-----------------------------------
    


#-----------------------------------
#   finish Quiz 
#-----------------------------------
class Sitting_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    class Meta():
        model = Sitting
        fields = ('id', 'user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end', 'get_percent_correct', 'check_if_passed', 'result_message', 'questions_with_user_answers', 'get_max_score')
        read_only_fields = ('id')



class Sitting_Update_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    get_percent_correct = serializers.IntegerField(required=False, default=0)
    check_if_passed = serializers.BooleanField(required=False, default=False)
    result_message = serializers.CharField(required=False, allow_blank=True, default='')
    questions_with_user_answers = serializers.CharField(required=False,allow_blank=True ,default='')
    get_max_score = serializers.IntegerField(required=False)

    class Meta():
        model = Sitting
        fields = ('id', 'user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end', 'get_percent_correct', 'check_if_passed', 'result_message', 'questions_with_user_answers', 'get_max_score')
        read_only_fields = ('id')

class Progress_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    class Meta():
        model = Progress
        fields = ('id', 'user', 'score', 'list_all_cat_scores')