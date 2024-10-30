from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Exercise
from .forms import ExerciseGoalForm, ExerciseResultForm

#　登録完了後の画面
def create_done(request):
  return render(request, "create_done.html")

# 運動目標登録画面のView
class ExerciseGoalView(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  form_class = ExerciseGoalForm
  template_name = "exercise_habits/goal_form.html"
  # 登録完了後の遷移先
  success_url = reverse_lazy("exerciseHabitsRecord:create_done")
  
  def get_context_data(self, **kwargs):
    context = super(ExerciseGoalView, self).get_context_data(**kwargs)
    context["message_type"] = "create_goal"
    return context
  
  def form_valid(self, form):
    messages.success(self.request, "運動目標の登録が完了しました。")
    return super().form_valid(form)
  
  def post(self, request, *args, **kwargs):
    user = request.user
    data = request.POST.dict()
    data["user"] = user.id
    form = ExerciseGoalForm(data=data)
    if form.is_valid():
      return self.form_valid(form)
    else:
      return self.form_invalid(form)

# 運動実績登録画面のView
class ExerciseResultView(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy("exerciseHabitsRecord:login")
  model = Exercise
  form_class = ExerciseResultForm
  template_name = "exercise_habits/result_form.html"
  # 登録完了後の遷移先
  success_url = reverse_lazy("exerciseHabitsRecord:create_done")

  def get_context_data(self, **kwargs):
    context = super(ExerciseResultView, self).get_context_data(**kwargs)
    context["message_type"] = "create_result"
    return context
  
  def form_valid(self, form):
    messages.success(self.request, "運動実績の登録が完了しました。")
    return super().form_valid(form)
  
  def post(self, request, *args, **kwargs):
    user = request.user
    data = request.POST.dict()
    data["user"] = user.id
    form = ExerciseResultForm(data=data)
    if form.is_valid():
      return self.form_valid(form)
    else:
      return self.form_invalid(form)

# ログイン画面
class LoginView(LoginView):
  template_name = "login.html"

# ログアウト画面
class LogoutView(LoginRequiredMixin, LogoutView):
  template_name = "login.html"