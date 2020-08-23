import nested_admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MNRUserCreationForm, MNRUserChangeForm
from .models import User, QuizTaker, Quiz, Question, Answer, UsersAnswer


class UserProfileInline(admin.StackedInline):
    model = QuizTaker
    can_delete = False
    verbose_name_plural = 'Quiz Taker'
    fk_name = 'user'
    # fieldsets = (
    #     ('Personal', {'fields': ('telephone',)}),
    #     ('Address', {'fields': ('address_street',
    #                             'address_number', 'zip_code', 'municipality', 'city', 'country')}),
    #     ('Status', {'fields': ('email_verified', 'reported', 'deleted')}),
    #     ('Favourited', {'fields': ('favorited', )})
    # )


class MNRUserAdmin(UserAdmin):
    add_form = MNRUserCreationForm
    form = MNRUserChangeForm
    model = User
    inlines = (UserProfileInline,)
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, MNRUserAdmin)


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline, ]
    extra = 5


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline, ]


class UsersAnswerInline(admin.TabularInline):
    model = UsersAnswer


class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [UsersAnswerInline, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(UsersAnswer)
