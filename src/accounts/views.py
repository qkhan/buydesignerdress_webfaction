from django.contrib.auth import login, get_user_model, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserCreationForm, UserLoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.db.models import Q
import pdb

User = get_user_model()
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print(request.user.profile.city)
        return render(request, "accounts/home.html", {})


def register(request, *args, **kwargs):
    # print ("Register: QAISAR KHAN")
    # print("Register:Request ISAJAX")
    # print(request.is_ajax)
    # print("Request POST")
    # print(request.POST)
    if request.POST:
        for key, value in request.POST.items():
            print("KEY:", key, " VALUE: ", value)
    # return render(request, "accounts/register.html", {})
    # print("Qaisar")
    # print (request.POST.get('login_or_register'))
    # #form = UserCreationForm(data=request.POST or None)
    # print ("Is form valid : FORM 1")
    # print (form.is_valid())
    #pdb.set_trace()

    if request.POST.get('login_or_register') == 'register':
        form = UserCreationForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            print("user created")
            form2 = UserLoginForm()
            return HttpResponseRedirect("/register")
    else:
        form = UserCreationForm(None)

    #form2 = UserLoginForm(data=request.POST or None)
    print ("Is form valid : FORM 1")
    print (form.is_valid())
    #pdb.set_trace()
    if request.POST.get('login_or_register') == 'login':
        form2 = UserLoginForm(data=request.POST or None)
        if form2.is_valid():
            # pdb.set_trace()
            form = UserCreationForm()
            print("user created")
            user_obj = form2.cleaned_data.get('user_obj')
            login(request, user_obj)
            return HttpResponseRedirect("/")
    else:
        form2 = UserLoginForm(None)


    return render(request, "accounts/register.html", {"form": form, "form2": form2})

    # form2 = UserLoginForm(data=request.POST or None)
    # print ("FORM VALID: ", form2.is_valid())
    # #pdb.set_trace()
    # if form2.is_valid():
    #     # pdb.set_trace()
    #     print("user created")
    #     user_obj = form2.cleaned_data.get('user_obj')
    #
    #     login(request, user_obj)
    #
    #     return HttpResponseRedirect("/")
    # else:
    #     messages.error(request, "Error")
    #     form2 = UserLoginForm()
    #
    # return render(request, "accounts/register.html", {"form": form, "form2": form2})


# class UserLoginForm(forms.Form):
#     query = forms.CharField(label='Username / Email')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         query = self.cleaned_data.get("query")
#         password = self.cleaned_data.get("password")

#         user_qs_final = User.objects.filter(
#                 Q(username__iexact=query) |
#                 Q(email__iexact=query)
#             ).distinct()
#         if not user_qs_final.exists() and user_qs_final.count != 1:
#             raise forms.ValidationError("Invalid Credentials -- User does not exists")

#         user_obj = user_qs_final.first()
#         if not user_obj.check_password(password):
#             raise forms.ValidationError("Invalid Credentials -- invalid Password")

#         if not user_obj.is_active:
#             raise forms.ValidationError("Inactive User")

#         self.cleaned_data["user_obj"] = user_obj
#         return super(UserLoginForm, self).clean(*args, **kwargs)


def user_login(request):
    query = password = ''
    response_data = {}
    print("Request ISAJAX")
    print(request.is_ajax)
    print("Request POST")
    print(request.POST)
    if request.POST and request.is_ajax:
        for key, value in request.POST.items():
            print("KEY:", key, " VALUE: ", value)
        query = request.POST['query']
        password = request.POST['password']
        user_qs_final = User.objects.filter(
        Q(username__iexact=query) |
        Q(email__iexact=query)
        ).distinct()

        print ("User QS Final:", user_qs_final)
        if not user_qs_final.exists() and user_qs_final.count != 1:
            response_data = {'user' : "nouser" }
            return HttpResponse(JsonResponse(response_data))
        user_obj = user_qs_final.first()
        print ("User Obj:", user_obj.username)
        print (user_obj.check_password(password))
        print ("Password")
        #pdb.set_trace()
        if not user_obj.check_password(password):
            if request.POST['data_from_form'] == "Y":
                return render(request, "accounts/register.html", {"message": "Wrong Password", "error": "Y"})
            else:
                response_data = {'user' : "password wrong" }
                print("Response:", response_data)
                return HttpResponse(JsonResponse(response_data))
        if not user_obj.is_active:
            if request.POST['data_from_form'] == "Y":
                return render(request, "accounts/register.html", {"message": "User is not active", "error": "Y"})
            else:
                response_data = {'user' : "not active" }
                return HttpResponse(JsonResponse(response_data))
        else:
            login(request, user_obj)
            if request.POST['data_from_form'] == "Y":
                return HttpResponseRedirect("/")
            else:
                response_data = {'login': "Success"}
                return HttpResponse(JsonResponse(response_data))
    else:
        query = password = ''
        response_data = {'login': "Failed"}
    return HttpResponse(JsonResponse(response_data))

def user_login_djuser(request, *args, **kwargs):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		# print("user created")
		user_obj = form.cleaned_data.get('user_obj')
		login(request, user_obj)
		return HttpResponseRedirect("/")
	return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/login")
