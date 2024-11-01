# Generated by Django 4.2.16 on 2024-10-29 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "user_id",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="利用者ID"
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="氏名")),
                (
                    "password",
                    models.CharField(max_length=20, verbose_name="パスワード"),
                ),
                (
                    "birth_day",
                    models.DateField(blank=True, null=True, verbose_name="生年月日"),
                ),
                (
                    "height",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        verbose_name="身長",
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=5,
                        null=True,
                        verbose_name="体重",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="email"),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="first_name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="last_name"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="is_superuer"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updateded_at"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("exercise_date", models.DateField(verbose_name="運動日")),
                (
                    "exercise_goal_1",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動目標1"
                    ),
                ),
                (
                    "goal_count_minutes_1",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="目標回数/時間1"
                    ),
                ),
                (
                    "exercise_goal_2",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動目標2"
                    ),
                ),
                (
                    "goal_count_minutes_2",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="目標回数/時間2"
                    ),
                ),
                (
                    "exercise_goal_3",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動目標3"
                    ),
                ),
                (
                    "goal_count_minutes_3",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="目標回数/時間3"
                    ),
                ),
                (
                    "exercise_result_1",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動実績1"
                    ),
                ),
                (
                    "result_count_minutes_1",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="実績回数/時間1"
                    ),
                ),
                (
                    "exercise_result_2",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動実績2"
                    ),
                ),
                (
                    "result_count_minutes_2",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="実績回数/時間2"
                    ),
                ),
                (
                    "exercise_result_3",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="運動実績3"
                    ),
                ),
                (
                    "result_count_minutes_3",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="実績回数/時間3"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="利用者",
                    ),
                ),
            ],
            options={
                "verbose_name": "運動情報",
                "verbose_name_plural": "運動情報",
                "db_table": "exercise",
            },
        ),
    ]
