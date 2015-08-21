from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


#questions
routerQuestions = format_suffix_patterns([
	url(r'^createTrueFalse$', True_False_Create_View.as_view() , name='createTrueFalse'),
	url(r'^listTrueFalse$', True_False_List_View.as_view() , name='listTrueFalse'),

	url(r'^createMultichoice$', Multichoice_Create_View.as_view() , name='createMultichoice'),
	url(r'^listMultichoice$', Multichoice_List_View.as_view() , name='listMultichoice'),

	url(r'^createAnswerMultichoice$', Multichoice_Answer_Create.as_view() , name='createMultichoice'),
	url(r'^MultichoiceAnswerList/(?P<pk>[0-9]+)/$', Multichoice_Answer_List_View.as_view() , name='createMultichoice'),

	url(r'^createEssay$', Essay_Create_View.as_view() , name='createEssay'),
	url(r'^listEssay$', Essay_List_View.as_view() , name='listEssay'),

	url(r'^/detail/(?P<pk>[0-9]+)/$', Question_Detail_View.as_view() , name='questionDetail'),
	])


#category
routerCategory = format_suffix_patterns([
	
	url(r'^createCategory$', Category_Create_View.as_view() , name='createCategory'),
	url(r'^listCategory$', Category_List_View.as_view() , name='listCategory'),	

	url(r'^createSubcategory$', Subcategory_Create_View.as_view() , name='createSubcategory'),
	url(r'^listSubcategory$', Subcategory_List_View.as_view() , name='listSubcategory'),

	])		

#Quiz
routerQuiz = format_suffix_patterns([
	
	url(r'^createQuiz$', Quiz_Create_View.as_view() , name='createQuiz'),
	url(r'^listQuiz$', Quiz_List_View.as_view() , name='listQuiz'),
	url(r'^listQuizbyCategory/(?P<category_name>[\w.-]+)$', Quiz_List_by_Category_View.as_view() , name='listQuizbyCategory'),
	url(r'^detail/(?P<pk>[0-9]+)/$', Quiz_Detail_View.as_view({'get': 'retrieve'}), name='detailQuiz'),
	url(r'^marking$', Quiz_Marking_List_View.as_view(), name='markingQuiz'),
	url(r'^allSitting$', Quiz_Sitting_View.as_view(), name='Sitting'),
	url(r'^marking/detail/(?P<pk>[0-9]+)/$', Quiz_Marking_Detail_View.as_view({'get': 'retrieve'}), name='markingQuiz'),
	url(r'^take/(?P<pk_quiz>[0-9]+)/$', Quiz_Take_View.as_view(), name='takeQuiz'),
	url(r'^progress$', Quiz_User_Progress_View.as_view() , name='progressQuiz'),
	url(r'^progress/exams/(?P<pk>[0-9]+)/$',  Quiz_show_exams_View.as_view() , name='progressExamsQuiz'),
	])


urlpatterns = patterns('',
)