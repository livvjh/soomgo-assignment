from django.contrib import admin

from product.models import Product, Category

admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'parent_category',
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_category":
            kwargs["queryset"] = Category.objects.filter(parent_category__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
