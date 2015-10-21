from django.contrib import admin

from .models import Person

class PersonInline(admin.TabularInline):
    model = Person

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['your_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('your_name', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Person)