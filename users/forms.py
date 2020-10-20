from django.contrib.auth.forms import UserCreationForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name', 'patronymic', 'email',
                                                 'date_of_birth', 'is_dir', 'department_user',
                                                 'division_user', 'position', 'tel_number', 'short_tel_number')
