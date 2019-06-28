from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Item, Category, Brand, Prospect, Country, Color, ProductType
from .forms import ItemModelForm
class ItemAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'price', 'discount', 'cartDesc']
    fields = ('added_by', 'last_edited_by', 'slug', 'sku', 'title', 'price', 'discount', 'size', 'weight', 'cartDesc', 'shortDesc', 'materialAndCare', 'color', 'fitting', 'longDesc')

    #readonly_fields = ['updated', 'timestamp', 'added_by', 'last_edited_by']
    readonly_fields = ['updated', 'timestamp']
    form = ItemModelForm
    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Prospect)
admin.site.register(Country)
#admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductType)
#admin.site.register(MaterialAndCare)
# admin.site.register(OptionGroup)
# admin.site.register(Option)
# admin.site.register(ItemOptions)
