from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('user/<str:username>/', views.UserQuestionListView.as_view(), name='user-polls'),
    path('polls/<int:pk>/',views.QuestionDetailView.as_view(),name="detail"),
    path('polls/<int:pk>/results/',views.QuestionResultView.as_view(),name="results"),
    path('polls/<int:question_id>/vote/',views.vote,name="vote"),
    path('about/', views.about, name='about')
]
