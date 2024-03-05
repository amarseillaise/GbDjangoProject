from django.contrib import admin


class PriceCustomFilter(admin.SimpleListFilter):
    title = "По цене"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return [('cheap', 'Дёшево'), ('medium', 'Нормально'), ('expensive', 'Дорого')]

    def queryset(self, request, queryset):
        if self.value() == 'cheap':
            return queryset.filter(price__lte=10000.0)
        if self.value() == 'medium':
            return queryset.filter(price__range=(10000.01, 50000.0))
        if self.value() == 'expensive':
            return queryset.filter(price__gte=50000.1)
        return queryset