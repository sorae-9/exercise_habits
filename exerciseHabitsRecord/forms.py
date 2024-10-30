from django import forms
from .models import Exercise

class DateInput(forms.DateInput):
  input_type = "date"

# 運動情報登録画面用のフォーム
class ExerciseGoalForm(forms.ModelForm):
  class Meta:
    model = Exercise
    fields = ["user", "exercise_date", "exercise_goal_1", "goal_count_minutes_1", "exercise_goal_2", "goal_count_minutes_2", "exercise_goal_3", "goal_count_minutes_3"]
    widgets = {
      "exercise_date": DateInput(),
      "user": forms.HiddenInput()
    }

# 運動実績登録画面用のフォーム
class ExerciseResultForm(forms.ModelForm):
  class Meta:
    model = Exercise
    fields = ["user", "exercise_date", "exercise_result_1", "result_count_minutes_1", "exercise_result_2", "result_count_minutes_2", "exercise_result_3", "result_count_minutes_3"]
    widgets = {
      "exercise_date": DateInput(),
      "user": forms.HiddenInput()
    }