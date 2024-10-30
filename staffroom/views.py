from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from exerciseHabitsRecord.models import Exercise
from exerciseHabitsRecord.forms import ExerciseGoalForm, ExerciseResultForm

# 更新完了後の画面
def update_done(request):
  return render(request, "update_done.html")

# 削除完了後の画面
def delete_done(request):
  return render(request, "delete_done.html")

# 運動記録一覧画面のView
class ExerciseHabitsList(LoginRequiredMixin, ListView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  template_name = "exercise_habits/list_form.html"
  def get_context_data(self, **kwargs):
    context = super(ExerciseHabitsList, self).get_context_data(**kwargs)
    if self.request.user.is_authenticated:
      context["exercise_list"] = Exercise.objects.filter(user=self.request.user)
    else:
      context["exercise_list"] = None
    return context

# 運動目標更新画面のView
class ExerciseGoalUpdateView(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  form_class = ExerciseGoalForm
  template_name = "exercise_habits/goal_form.html"
  # 更新完了後の遷移先
  success_url = reverse_lazy("staffroom:exerciseHabitsRecord:update_done")
  def get_context_data(self, **kwargs):
    context = super(ExerciseGoalUpdateView, self).get_context_data(**kwargs)
    context["message_type"] = "update_goal"
    return context
  
  def form_valid(self, form):
    messages.success(self.request, "運動目標の更新が完了しました。")
    return super().form_valid(form)


# 運動実績更新画面のView
class ExerciseResultUpdateView(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  form_class = ExerciseResultForm
  template_name = "exercise_habits/result_form.html"
  # 更新完了後の遷移先
  success_url = reverse_lazy("staffroom:exerciseHabitsRecord:update_done")
  def get_context_data(self, **kwargs):
    context = super(ExerciseResultUpdateView, self).get_context_data(**kwargs)
    context['message_type'] = "update_result"
    return context
  
  def form_valid(self, form):
    messages.success(self.request, "運動実績の更新が完了しました。")
    return super().form_valid(form)

# 運動情報削除画面のView
class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  template_name = "delete_form.html"
  # 削除完了後の遷移先
  success_url = reverse_lazy("staffroom:exerciseHabitsRecord:delete_done")
  def get_context_data(self, **kwargs):
    context = super(ExerciseDeleteView, self).get_context_data(**kwargs)
    context['message_type'] = "delete_exercise"
    return context
