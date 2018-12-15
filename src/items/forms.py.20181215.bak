from django import forms
from .models import Item
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from floppyforms import ClearableFileInput
from ckeditor.widgets import CKEditorWidget

SOME_CHOICES = [
    ('db-value', 'Display Value'),
    ('db-value2', 'Display Value2'),
    ('db-value3', 'Display Value3'),
]


INTS_CHOICES = [tuple([x,x]) for x in range(0, 102)]

YEARS = [x for x in range(1980, 2031)]

class ImageThumbnailFileInput(ClearableFileInput):
    template_name = 'floppyforms/image_thumbnail.html'

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
        "categoryID",
        "brandID",
        "prospectID",
        "countryID",
        "slug",
        "sku",
        "title",
        "price",
        "size",
        "color",
        "weight",
        "cartDesc",
        "shortDesc",
        "materialAndCare",
        "fitting",
        "longDesc",
        "stock",
        "live",
        "itemLimited",
        "location",
        "featured",
        "active",
        "thumb_image",
        "image1",
        "image2",
        "image3",
        "image4",
        "image5",
        "image6",

        ]
        #"added_by",
        #"last_edited_by",
         #answer = forms.CharField(label="Answer",
        #widget=forms.TextInput(attrs={'autofocus': 'autofocus',
        #                              'autocomplete': 'off',
        #                              'size': '40',
        #                              'font-size': 'xx-large',
        #                              }))
        widgets = {
          # 'email': forms.EmailInput(attrs={'class': 'form-control custom-class'}),
          'categoryID' : forms.Select(attrs={'class': 'form-control custom-class'}),
          'brandID' : forms.Select(attrs={'class': 'form-control custom-class'}),
          'prospectID' : forms.Select(attrs={'class': 'form-control custom-class'}),
          'countryID' : forms.Select(attrs={'class': 'form-control custom-class'}),
          'slug': forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'sku': forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'title': forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
          'size': forms.SelectMultiple(attrs={'class': 'form-control custom-class'}),
          'color': forms.Select(attrs={'class': 'form-control custom-class'}),
          'weight': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
          'cartDesc': forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'shortDesc': CKEditorWidget(config_name='default'),
          'materialAndCare': CKEditorWidget(config_name='default'),
          'fitting': CKEditorWidget(config_name='default'),
          'longDesc': CKEditorWidget(config_name='default'),
          'stock': forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'live' : forms.CheckboxInput(attrs={'class': 'form-control custom-class', 'style': 'margin-top: -6px;'}),
          'itemLimited': forms.CheckboxInput(attrs={'class': 'form-control custom-class', 'style': 'margin-top: -6px;'}),
          'location' : forms.TextInput(attrs={'class': 'form-control custom-class'}),
          'featured': forms.CheckboxInput(attrs={'class': 'form-control custom-class', 'style': 'margin-top: -6px;'}),
          'active' : forms.CheckboxInput(attrs={'class': 'form-control custom-class', 'style': 'margin-top: -6px;'}),
          'thumb_image' : ImageThumbnailFileInput,
          'image1' : ImageThumbnailFileInput,
          'image2' : ImageThumbnailFileInput,
          'image3' : ImageThumbnailFileInput,
          'image4' : ImageThumbnailFileInput,
          'image5' : ImageThumbnailFileInput,
          'image6' : ImageThumbnailFileInput,



          # 'updateDate': forms.DateTimeField(attrs={'class': 'form-control custom-class'}),
          # 'timestamp': forms.DateTimeField(attrs={'class': 'form-control custom-class'}),

        }
        exclude = ["height_field","width_field"]
        labels = {
            "categoryID": mark_safe("<strong>Dress Category</strong>"),
            "brandID": mark_safe("<strong>Brand Name</strong>"),
            "prospect": mark_safe("<strong>Prospect</strong>"),
            "country": mark_safe("<strong>Country</strong>"),
            "slug": mark_safe("<strong>Product Slug</strong>"),
            "sku": mark_safe("<strong>SKU</strong>"),
            "title": mark_safe("<strong>Product Name</strong>"),
            "price": mark_safe("<strong>Price</strong>"),
            "size": mark_safe("<strong>Size</strong>"),
            "color": mark_safe("<strong>Color</strong>"),
            "weight": mark_safe("<strong>Product Weight</strong>"),
            "cartDesc": mark_safe("<strong>Cart Description</strong>"),
            "shortDesc": mark_safe("<strong>Product Short Description</strong>"),
            "materialAndCare": mark_safe("<strong>Material And Care</strong>"),
            "fitting": mark_safe("<strong>Fitting</strong>"),
            "longDesc": mark_safe("<strong>Product Detailed Description</strong>"),
            "stock": mark_safe("<strong>Stock</strong>"),
            "live": mark_safe("<strong>Live Product</strong>"),
            "itemLimited": mark_safe("<strong>Product is Limited</strong>"),
            "location": mark_safe("<strong>Product Location</strong>"),
            "featured": mark_safe("<strong>Product Feature</strong>"),
            "active": mark_safe("<strong>Is Product Active</strong>"),
            "thumb_image": mark_safe("<strong>Thumbnail</strong>"),
            "image1": mark_safe("<strong>Product Image 1</strong>"),
            "image2": mark_safe("<strong>Product Image 2</strong>"),
            "image3": mark_safe("<strong>Product Image 3</strong>"),
            "image4": mark_safe("<strong>Product Image 4</strong>"),
            "image5": mark_safe("<strong>Product Image 5</strong>"),
            "image6": mark_safe("<strong>Product Image 6</strong>"),
        }
        help_text = {
            "title": "this is title label",
            "slug": "This is slug",
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long.",
                "required": "This title field is required",
            },
            "slug": {
                "max_length": "This title is too long",
                "required": "This title field is required",
                "unique" :  "The slug field must be unique",
            }
        }

    def __init__(self, *args, **kwargs):
        super(ItemModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].error_messages = {
                "max_length": "This title is too long.",
                "required": "This title field is required",
        }
        self.fields["slug"].error_messages = {
                "max_length": "This title is too long.",
                "required": "This title field is required",
        }

        for field in self.fields.values():
            field.error_messages = {
                'required': "You know, {fieldname} is required".format(fieldname=field.label),
            }

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        print (title)
        return title

    def save(self, commit=True, *args, **kwargs):
        obj = super(ItemModelForm, self).save(commit=False, *args, **kwargs)
        obj.slug = slugify(obj.title)
        obj.publish = "2018-05-04"
        print("TITLE: ", obj.title)
        if commit:
            obj.save()
        return obj

# class TestForm(forms.Form):
#     date_field = forms.DateField(initial="2010-11-20", widget=SelectDateWidget(years=YEARS))
#     some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows": 4, "cols": 10}))
#     choices = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES))
#     boolean = forms.BooleanField()
#     integer = forms.IntegerField(initial=101, widget=forms.Select(choices=INTS_CHOICES))
#     email = forms.EmailField(min_length=10)
#
#
#     def __init__(self, user=None, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         print("QK", user)
#         if user:
#             self.fields["some_text"].initial = user.username
#
#     def clean_integer(self, *args, **kwargs):
#         integer = self.cleaned_data.get("integer")
#         if integer < 10:
#             raise forms.ValidationError("The integer must be greater than 10")
#         return integer
#
#     def clean_some_text(self, *args, **kwars):
#         some_text = self.cleaned_data.get("some_text")
#         if len(some_text) < 5:
#             raise forms.ValidationError("Ensure the text is greater than 5 characters")
#         return some_text
