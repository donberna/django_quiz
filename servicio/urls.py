from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
	#questions
	url(r'^createTrueFalse$', True_False_Create_View.as_view() , name='createTrueFalse'),
	url(r'^listTrueFalse$', True_False_List_View.as_view() , name='listTrueFalse'),

	url(r'^createMultichoice$', Multichoice_Create_View.as_view() , name='createMultichoice'),
	url(r'^listMultichoice$', Multichoice_List_View.as_view() , name='listMultichoice'),

	url(r'^createEssay$', Essay_Create_View.as_view() , name='createEssay'),
	url(r'^listEssay$', Essay_List_View.as_view() , name='listEssay'),

	#category
	url(r'^createCategory$', Category_Create_View.as_view() , name='createCategory'),
	url(r'^listCategory$', Category_List_View.as_view() , name='listCategory'),	

	url(r'^createSubcategory$', Subcategory_Create_View.as_view() , name='createSubcategory'),
	url(r'^listSubcategory$', Subcategory_List_View.as_view() , name='listSubcategory'),
	
	#Quiz
	url(r'^createQuiz$', Quiz_Create_View.as_view() , name='createQuiz'),
	url(r'^listQuiz$', Quiz_List_View.as_view() , name='listQuiz'),
	url(r'^listQuizbyCategory/(?P<category_name>[\w.-]+)$', Quiz_List_by_Category_View.as_view() , name='listQuizbyCategory'),
	url(r'^quiz/detail/(?P<pk>[0-9]+)/$', Quiz_Detail_View.as_view({'get': 'retrieve'}), name='detailQuiz'),
	url(r'^marking$', Quiz_Marking_List_View.as_view(), name='markingQuiz'),
	url(r'^marking/detail/(?P<pk>[0-9]+)/$', Quiz_Marking_Detail_View.as_view({'get': 'retrieve'}), name='markingQuiz'),
	#url(r'^(?P<quiz_name>[\w-]+)/take/$', Quiz_Take_View.as_view(), name='takeQuiz'),
	url(r'^progress$', Quiz_User_Progress_View.as_view() , name='progressQuiz'),
)