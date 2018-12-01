from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, \
                        TemplateResponseMixin, \
                        ContextMixin
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,\
                        UpdateView, \
                        DeleteView, \
                        ModelFormMixin

from django.utils import timezone
from .models import Item
from .forms import ItemModelForm

class LoginRequiredMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LoginRequiredMixin, cls).as_view(**kwargs)
    #     return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class MultipleObjectMixin(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print("SLUG:", slug)
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            except:
                raise Http404
            return obj
        raise Http404


class ItemDeleteView(MultipleObjectMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')

class ItemUpdateView(MultipleObjectMixin, UpdateView):
    model = Item
    form_class = ItemModelForm
    template_name = "forms.html"

# def TestView(request):
#     form = TestForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         print(form.cleaned_data.get("some_text"))
#         print(form.cleaned_data.get("email"))
#         print(form.cleaned_data.get("email2"))
#
#     return render(request, "forms.html", {"form": form})


class ItemCreateView(SuccessMessageMixin, MultipleObjectMixin, CreateView):
    #print("QAISAR KHAN")
    form_class = ItemModelForm
    #model = Item
    #template_name = "manual_form.html"
    template_name = "forms.html"
    success_message = "%(title)s has been created at %(created_at)s"
    #to add new fields to the model

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("item_list")

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at=self.object.timestamp,
        )

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'Qaisar Khan'
        return context


class MyView(LoginRequiredMixin, ContextMixin, TemplateResponseMixin, View):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'Some other Title'
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MyView, self).dispatch(request, *args, **kwargs)


class ItemListView(ListView):
    print ("Item List View")
    model = Item

    def get_queryset(self, *args, **kwargs):
        #qs = super(BookListView, self).get_queryset(*args, **kwargs).filter(title__startswith="Ye")
        qs = super(ItemListView, self).get_queryset(*args, **kwargs).order_by("-timestamp")

        #print (qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ItemDetailView(SuccessMessageMixin, ModelFormMixin, MultipleObjectMixin, DetailView):

    model = Item
    form_class = ItemModelForm
    success_message = "%(title)s has been updated."

    #template_name = "manual_form.html"
    template_name = "forms.html"
    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetailView, self).get_context_data(*args, **kwargs)
        context["form"] = self.get_form()
        context['now'] = timezone.now()
        context['btn_title'] = "Update Product Detail"
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        form = self.get_form()
        if form.is_valid():
            ###image = form.cleaned_data["thumb"]
            #print ("IMAGE:", image)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("item_list")
