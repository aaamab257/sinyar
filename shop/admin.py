from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group , User
from modeltranslation.admin import TranslationAdmin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from reportlab.pdfgen import canvas


admin.site.disable_action("delete_selected")



@admin.action(description='Download PDF report')
def download_pdf_report(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="product_report.pdf"'

    # Create the PDF report
    p = canvas.Canvas(response)
    p.drawString(100, 750, "Report")
    p.drawString(100, 700, "=" * 20)

    for i, product in enumerate(queryset):
        p.drawString(100, 650 - i * 50, f"Product name: {product.name}")
        p.drawString(100, 625 - i * 60, f"Price: {product.price}")
        p.drawString(100, 600 - i * 70, f"Description: {product.description}")
        p.drawString(100, 575 - i * 80, f"Category: {product.category.name}")
        p.drawString(100, 550 - i * 90, f"SubCategory: {product.subcategory.name}")
        p.drawString(100, 525 - i * 100, f"Vendor: {product.seller}")
        
        

    p.showPage()
    p.save()

    return response


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}
    group_fieldsets = True
    list_display = ('name', 'parent')
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Vendor)
class SubCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'name': ('name',)}
    list_display = ('name', 'email')
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'subcategory', 'price' , 'seller')
    actions = [download_pdf_report]
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }





    


@admin.action(description="Mark selected requests as accepted")
def accept_request(modeladmin, request, queryset):
    queryset.update(status="a")


@admin.action(description="Mark selected requests as refused")
def refuse_request(modeladmin, request, queryset):
    queryset.update(status="r")


class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ['user','plan' , 'product']
    list_display = ["user", "status"]
    ordering = ["user" , "status"]
    actions = [accept_request ,refuse_request ]
    


admin.site.register(Request, RequestAdmin)

admin.site.register(IntrestedCategory)



