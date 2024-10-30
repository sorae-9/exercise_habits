from django.urls import path, include  
from ..views import ExerciseHabitsList

app_name = "staffroom"

urlpatterns = [
  path("", ExerciseHabitsList.as_view(), name="index"),
  path("exercise_habits/", include("staffroom.urls.exercise_habits", namespace="exerciseHabitsRecord")), 
]