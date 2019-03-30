from django.shortcuts import render

# Create your views here.


def checkout_address_create_view(request, *args, **kwargs):
    form = GuestForm(request.POST or None)
    print("Form QAISAR")
    print(form)
    context = {
        "form": form
    }
    print("Request")
    print(request)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("http://buydesignerdress.com/cart/")

    return redirect("/register/")

