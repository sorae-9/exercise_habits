from django.contrib import admin
from exerciseHabitsRecord.models import Exercise

# adminサイト 運動情報一覧 表示項目
class ExerciseAdmin(admin.ModelAdmin):
  list_display = ("user_id", "exercise_date", "exercise_goal_1", "goal_count_minutes_1", "exercise_result_1", "result_count_minutes_1")

admin.site.register(Exercise, ExerciseAdmin)
