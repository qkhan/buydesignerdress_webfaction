from django import forms
#from django.forms import extras
#from extras.widgets import SelectDateWidget
from .models import Product
from django.utils.text import slugify

SOME_CHOICES = [
    ('db-value', 'Display Value'),
    ('db-value2', 'Display Value2'),
    ('db-value3', 'Display Value3'),
]


INTS_CHOICES = [tuple([x,x]) for x in range(0, 102)]

YEARS = [x for x in range(1980, 2031)]



# class ProductModelForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             "slug",
#             "productSKU",
#             "productName",
#             "productPrice",
#             "productWeight",
#             "productCartDesc",
#             "productShortDesc",
#             "productLongDesc",
#             "productThumb",
#             "productImage1",
#             "productImage2",
#             "productImage3",
#             "productCategoryID",
#             "productUpdateDate",
#             "productTimestamp",
#             "productStock",
#             "productLive",
#             "ProductLimited",
#             "ProductLocation"
#             "featured",
#             "active",
#         ]
#         exclude = ["height_field","width_field", "productWeight"]
#         labels = {
#             "slug" : "Unique Slug",
#             "productSKU": "Product SKU",
#             "productName": "Name",
#             "productCategoryID": "Category",
#             "productPrice": "Price",
#             "productCartDesc": "Cart Description",
#             "productShortDesc": "Short Description",
#             "productLongDesc": "Detailed Description",
#             "productThumb": "Product Thumb",
#             "productImage1": "Product Image 1",
#             "productImage2": "Product Image 2",
#             "productImage3": "Product Image 3",
#             "productUpdateDate": "Update Date",
#             "productTimestamp": "Added Date",
#             "productStock": "Stock Available",
#             "productLive": "Product Live",
#             "ProductLimited" : "Product Limited",
#             "ProductLocation": "Location",
#             "featured": "Featured",
#             "active": "Active",
#         }
#         help_text = {
#             "productName": "this is product name label",
#         }
#         error_messages = {
#             "productName": {
#                 "max_length": "This product name is too long.",
#                 "required": "The product name is required",
#             },
#         }
#
#     # def __init__(self, *args, **kwargs):
#     #     super(PostModelForm, self).__init__(*args, **kwargs)
#     #     self.fields["title"].error_messages = {
#     #             "max_length": "This title is too long.",
#     #             "required": "This title field is required",
#     #     }
#     #     self.fields["slug"].error_messages = {
#     #             "max_length": "This title is too long.",
#     #             "required": "This title field is required",
#     #     }
#     #
#     #     for field in self.fields.values():
#     #         field.error_messages = {
#     #             'required': "You know, {fieldname} is required".format(fieldname=field.label),
#     #         }
#
#     def clean_productName(self, *args, **kwargs):
#         productName = self.cleaned_data.get("productName")
#         print (productName)
#         return productName
#
#     # def save(self, commit=True, *args, **kwargs):
#     #     obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
#     #     obj.slug = slugify(obj.title)
#     #     obj.publish = "2018-05-04"
#     #     if commit:
#     #         obj.save()
#     #     return obj
#
# class TestForm(forms.Form):
#     date_field = forms.DateField(initial="2010-11-20", widget=forms.extras.widgets.SelectDateWidget(years=YEARS))
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
