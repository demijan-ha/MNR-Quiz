from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Quiz, Category, Question, Progress, AnonProgress, Sitting, AnonSitting, UserProfile
from mcq.models import MCQQuestion, Answer
from django.utils.translation import gettext as _


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('description', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category',)


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category',)
    list_filter = ('category',)
    fields = ('content', 'category',
              'figure', 'quiz', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]


class ProgressAdmin(admin.ModelAdmin):
    search_fields = ('user', 'score',)


class AnonProgressAdmin(admin.ModelAdmin):
    pass


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    readonly_fields = ['start', 'end']
    fieldsets = (
        ('Profile details',
         {'fields':
              ('country', 'city', 'address', 'zip_code')
          }
         ),
        ('Quiz details',
         {'fields':
              ('score', 'start', 'end')
          }
         ),
    )


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = (UserProfileInline,)
    list_select_related = ('profile',)
    list_display = ('email', 'first_name', 'last_name', 'country', 'score', 'time_finished')
    list_filter = ('profile__country',)
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
    search_fields = ('email', 'profile__country', 'first_name', 'last_name')
    ordering = ('email', )

    def score(self, obj):
        return obj.profile.score
    score.admin_order_field = 'profile__score'

    def country(self, obj):
        return obj.profile.country.name
    country.admin_order_field = 'profile__country'

    def time_finished(self, obj):
        return obj.profile.end
    time_finished.admin_order_field = 'profile__end'


admin.site.register(User, CustomUserAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MCQQuestion, MCQuestionAdmin)

