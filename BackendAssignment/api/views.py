from django.shortcuts import render
from django.views import View
from .auth import Auth
from .forms import Login

# Create your views here.
class LoginView(View):
    template_name = "login.html"
    form_class = Login

    # GET
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form": form})

    # POST
    def post(self, request):
        pass


class UserView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
