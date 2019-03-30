from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q

from django.utils import timezone

from items.models import Item


class SearchItemView(ListView):
    print ("Item List View")
    model = Item
    template_name = "search/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q', None)
        print(query)
        if query is not None:
            return Item.objects.search(query)
            #lookups = Q(title__icontains=query) | Q(short_description__incontains=query)
            #qs = super(SearchItemView, self).get_queryset(*args, **kwargs).filter(lookups)

            #qs = super(SearchItemView, self).get_queryset(*args, **kwargs).filter(lookups)
            #print (qs)
            #return qs
        else:
            return Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SearchItemView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

