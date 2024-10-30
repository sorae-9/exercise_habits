from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
  class Meta:
    db_table = "exercise"
    verbose_name = "運動情報"
    verbose_name_plural = "運動情報"

  user = models.ForeignKey(User, verbose_name = "利用者", on_delete=models.CASCADE, default=None, null=True)
  exercise_date = models.DateField(verbose_name = "運動日")
  exercise_goal_1 = models.CharField(verbose_name ="運動目標1", max_length=50, null=True, blank=True)
  goal_count_minutes_1 = models.PositiveSmallIntegerField(verbose_name ="目標回数/時間1", null=True, blank=True)
  exercise_goal_2 = models.CharField(verbose_name ="運動目標2", max_length=50, null=True, blank=True)
  goal_count_minutes_2 = models.PositiveSmallIntegerField(verbose_name ="目標回数/時間2", null=True, blank=True)
  exercise_goal_3 = models.CharField(verbose_name ="運動目標3", max_length=50, null=True, blank=True)
  goal_count_minutes_3 = models.PositiveSmallIntegerField(verbose_name ="目標回数/時間3", null=True, blank=True)
  exercise_result_1 = models.CharField(verbose_name ="運動実績1", max_length=50, null=True, blank=True)
  result_count_minutes_1 = models.PositiveSmallIntegerField(verbose_name ="実績回数/時間1", null=True, blank=True)
  exercise_result_2 = models.CharField(verbose_name ="運動実績2", max_length=50, null=True, blank=True)
  result_count_minutes_2 = models.PositiveSmallIntegerField(verbose_name ="実績回数/時間2", null=True, blank=True)
  exercise_result_3 = models.CharField(verbose_name ="運動実績3", max_length=50, null=True, blank=True)
  result_count_minutes_3 = models.PositiveSmallIntegerField(verbose_name ="実績回数/時間3", null=True, blank=True)

  # adminサイト一覧に表示される項目
  def __str__(self):
    return str(self.exercise_date)