from django.urls import path
from staffroom.views import (
  update_done, delete_done, ExerciseHabitsList, ExerciseGoalUpdateView, ExerciseResultUpdateView, ExerciseDeleteView
)

app_name = "exerciseHabitsRecord"

urlpatterns = [
    path('exercise_list', ExerciseHabitsList.as_view(), name="exercise_list"),
    path("update_goal/<int:pk>/", ExerciseGoalUpdateView.as_view(), name="update_goal"),
    path("delete_exercise/<int:pk>/", ExerciseDeleteView.as_view(), name="delete_exercise"),
    path("update_result/<int:pk>/", ExerciseResultUpdateView.as_view(), name="update_result"),
    path('update_done/', update_done, name='update_done'),
    path('delete_done/', delete_done, name='delete_done'),
]