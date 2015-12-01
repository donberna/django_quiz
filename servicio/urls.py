from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


#questions


routerQuestions = format_suffix_patterns([
	url(r'^createTrueFalse$', True_False_Create_View.as_view() , name='createTrueFalse'),
	url(r'^listTrueFalse$', True_False_List_View.as_view() , name='listTrueFalse'),
	url(r'^updateTrueFalse/(?P<pk>[0-9]+)/$', True_False_Update_View.as_view({'put': 'update', 'delete': 'destroy'}), name='updateTrueFalse'),

	url(r'^createMultichoice$', Multichoice_Create_View.as_view() , name='createMultichoice'),
	url(r'^listMultichoice$', Multichoice_List_View.as_view() , name='listMultichoice'),
	url(r'^updateMultichoice/(?P<pk>[0-9]+)/$', Multichoice_Update_View.as_view({'put': 'update', 'delete': 'destroy'}), name='updateMultichoice'),

	url(r'^createAnswerMultichoice$', Multichoice_Answer_Create.as_view() , name='createMultichoice'),
	url(r'^createMultipleAnswerMultichoice$', Multichoice_Answer_Create_multiple.as_view() , name='createMultichoice_many'),
	url(r'^updateMultipleAnswerMultichoice$', Multichoice_Answer_Update_multiple.as_view() , name='createMultichoice_many'),
	url(r'^MultichoiceAnswerList/(?P<pk>[0-9]+)/$', Multichoice_Answer_List_View.as_view() , name='createMultichoice'),

	url(r'^createEssay$', Essay_Create_View.as_view() , name='createEssay'),
	url(r'^listEssay$', Essay_List_View.as_view() , name='listEssay'),
	url(r'^updateEssay/(?P<pk>[0-9]+)/$', Essay_Update_View.as_view({'put': 'update', 'delete': 'destroy' }), name='updateEssay'),

	url(r'^detail/(?P<pk>[0-9]+)/$', Question_Detail_View.as_view() , name='questionDetail'),
	])


#category
#urls for Updating


#routerCategory = format_suffix_patterns([
		
	#url(r'^createCategory$', Category_Create_View.as_view() , name='createCategory'),
	#url(r'^listCategory$', Category_List_View.as_view() , name='listCategory'),	
	#url(r'^updateCategory/(?P<pk>[0-9]+)/$', Category_Update_View.as_view({'put': 'update', 'delete': 'destroy'}), name='updateCategory'),

	#url(r'^createSubcategory$', Subcategory_Create_View.as_view() , name='createSubcategory'),
	#url(r'^listSubcategory$', Subcategory_List_View.as_view() , name='listSubcategory'),
	#url(r'^updateSubCategory/(?P<pk>[0-9]+)/$', SubCategory_Update_View.as_view({'put': 'update', 'delete': 'destroy'}), name='updateSubCategory'),
	
	#])		


#Quiz
#urls for Updating

routerQuizDetail = Quiz_Update_View.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

from module.settings import MODULE_SLUG_PATTERN
routerQuiz = format_suffix_patterns([
	
	url(r'^createQuiz$', Quiz_Create_View.as_view() , name='createQuiz'),
	url(r'^listQuiz$', Quiz_List_View.as_view() , name='listQuiz'),
	#url(r'^listQuizbyCategory/(?P<category_name>[\w.-]+)$', Quiz_List_by_Category_View.as_view() , name='listQuizbyCategory'),
	
	
	# quiz end
	url(r'^marking$', Quiz_Marking_List_View.as_view(), name='markingQuiz'),
	url(r'^marking/detail/(?P<pk>[0-9]+)/$', Quiz_Marking_Detail_View.as_view({'get': 'retrieve'}), name='markingQuiz'),
	
	url(r'^(?P<slug>'+MODULE_SLUG_PATTERN+')/detail/(?P<pk>[0-9]+)/$', routerQuizDetail, name='detailQuiz'),
	
	#sitting
	url(r'^allSitting$', Quiz_Sitting_View.as_view(), name='Sitting'),
	url(r'^sitting/(?P<pk_quiz>[0-9]+)/$', Quiz_Create_Sitting_View.as_view(), name='takeQuiz'),
	url(r'^(?P<slug>'+MODULE_SLUG_PATTERN+')/updateSitting/(?P<pk>[0-9]+)/$', Quiz_update_sitting_View.as_view({'put': 'update'}), name='updateSitting'),

	# check quiz 
	url(r'^qualify$', Quiz_Qualify_View.as_view(), name='qualifyQuiz'),
	url(r'^(?P<slug>'+MODULE_SLUG_PATTERN+')/changeQualify$', Quiz_Sitting_Change_Qualify.as_view(), name='changeQualifyQuiz'),
	#url(r'^checkPassed$', Quiz_Check_Passed_View.as_view(), name='checkPassedQuiz'),
	
	#progress 
	url(r'^progress$', Quiz_User_Progress_View.as_view() , name='progressQuiz'),
	url(r'^progress/exams/(?P<pk>[0-9]+)/$',  Quiz_show_exams_View.as_view() , name='progressExamsQuiz'),
	])


urlpatterns = patterns('',
)