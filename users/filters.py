import django_filters
from django_filters.filters import OrderingFilter

from users.models import User


class UserFilter(django_filters.FilterSet):
    ordering = OrderingFilter(
        fields=(
            ('last_name', 'Прізвище'),
        )
    )

    class Meta:
        model = User
        fields = ['department_user', 'division_user', 'is_dir']
        ordering = ['last_name']
