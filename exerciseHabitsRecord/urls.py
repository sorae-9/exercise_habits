from django.urls import path
from .views import (
  ExerciseGoalView, ExerciseResultView, create_done, LoginView, LogoutView
)

app_name = "exerciseHabitsRecord"

urlpatterns = [
    path("goal/", ExerciseGoalView.as_view(), name="create_goal"),
    path("result/", ExerciseResultView.as_view(), name="create_result"),
    path("create_done", create_done, name="create_done"),
    path("login", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]