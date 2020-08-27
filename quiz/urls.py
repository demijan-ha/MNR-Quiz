from .views import *
from django.urls import path, re_path


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('signup/<uuid:uuid>', signup, name='signup'),
    path('quizzes/', QuizListView.as_view(), name='quiz_index'),
    path('quizzes/<slug:slug>/', QuizDetailView.as_view(), name='quiz_start_page'),
    path('quizzes/<slug:slug>/take/<uuid:uuid>', QuizTake.as_view(), name='quiz_question'),
    path('category/<int:pk>', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    path('category/', CategoriesListView.as_view(), name='quiz_category_list_all'),
    path('progress/', QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/<int:pk>/', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    path('marking/', QuizMarkingList.as_view(), name='quiz_marking'),

]
