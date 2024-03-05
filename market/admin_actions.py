from django.contrib import admin


@admin.action(description="Уменьшить количество на 1")
def change_quantity(modeladmin, request, queryset):
    for obj in queryset:
        obj.total_quantity -= 1
        obj.save()
