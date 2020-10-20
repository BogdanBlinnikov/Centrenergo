from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView

from .filters import UserFilter
from .forms import CustomUserCreationForm
from .models import User


class CreateUserView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    permission_required = 'users.registration'
    login_url = 'users:login'

    # def post(self, request, *args, **kwargs):
    #     res = super().post(request, *args, **kwargs)
    #     if self.object:
    #         login(user=self.object, request=request)
    #     return res

    def get_success_url(self):
        return reverse('users:profile', args=[self.object.id])

    def handle_no_permission(self):
        messages.error(self.request, 'You have no permission')
        return super(CreateUserView, self).handle_no_permission()


class LoginCreateView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse('users:profile', args=[self.request.user.id])


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


class ProfilesListView(LoginRequiredMixin, FilterView):
    # paginate_by = 10
    template_name = 'users/index.html'
    context_object_name = 'profiles_list'
    login_url = 'users:login'
    filterset_class = UserFilter

    # def get_queryset(self):
    #     return User.objects.all().order_by('last_name')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # context['filter'].qs = sorted(context['filter'].qs)
        return context

class ProfileView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_info'


class ProfileEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    fields = ['last_name', 'first_name', 'patronymic', 'email',
              'date_of_birth', 'is_dir', 'department_user',
              'division_user', 'position', 'tel_number', 'short_tel_number']
    template_name = 'users/edit_profile.html'
    permission_required = 'users.edit_profile'
    login_url = 'users:login'

    def get_success_url(self):
        return reverse('users:profile', args=[self.object.id])

    def handle_no_permission(self):
        messages.error(self.request, 'You have no permission')
        return super(ProfileEditView, self).handle_no_permission()
