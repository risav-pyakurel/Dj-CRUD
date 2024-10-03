from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    
    next_page = reverse_lazy('news:list')
    
    def form_invalid(self, form):
        messages.error(self.request, "Milne Credentials halna tori.")
        return super().form_invalid(form)
        
