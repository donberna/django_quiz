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

class TF_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create TF_Question
    """
    class Meta():
        model = TF_Question


class Create_Answer_MC_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Asks
    """
    
    class Meta():
        model = Answer
        fields = ('content', 'correct')


class Create_MC_Question_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create MCQuestion
    """
    # fields anwers
    answer = Create_Answer_MC_Question_Serializer(many=True)
    #print answer

    def create(self, validated_data):
        answer_content_data = validated_data.pop('content')
        answer_correct_data = validated_data.pop('correct')
        ans = Answer.objects.create(answer_correct_data,answer_content_data)
        mcquestion = MCQuestion.objects.create(answer = ans, **validated_data)        

        return MCQuestion.objects.create(answer = ans, **validated_data)
    #print answer"""

    class Meta():
        model = MCQuestion
        fields = ( 'id', 'quiz', 'category', 'sub_category', 'figure', 'content', 'explanation', 'objects', 'answer')
        read_only_fields = ('id')


class List_Multichoice_Serializer(serializers.ModelSerializer):
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
class Create_Sitting_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    """def create(self, *args, **kwargs):
        try:
            user = self.context['request'].user
            print user
            return Sitting.objects.create(user=user,quiz=quiz,question_order=questions,question_list=questions,incorrect_questions="",current_score=0,complete=False,user_answers='{}')

        except IntegrityError, e:
            raise PermissionDenied"""

    class Meta():
        model = Sitting
        fields = ('user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end', 'get_current_score', 'get_percent_correct', 'get_incorrect_questions', 'check_if_passed', 'result_message', 'questions_with_user_answers', 'get_max_score')

    


#-----------------------------------
#   finish Quiz 
#-----------------------------------

class Sitting_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    class Meta():
        model = Sitting
        fields = ('user', 'quiz', 'question_order', 'question_list', 'incorrect_questions', 'current_score', 'complete', 'user_answers', 'start', 'end', 'get_current_score', 'get_percent_correct', 'get_incorrect_questions', 'check_if_passed', 'result_message', 'questions_with_user_answers', 'get_max_score')


class Progress_Serializer(serializers.ModelSerializer):
    """
    Serializer Class to create Quiz
    """
    class Meta():
        model = Progress
        fields = ('id', 'user', 'score', 'list_all_cat_scores')