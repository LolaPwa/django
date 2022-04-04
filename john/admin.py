from django.contrib import admin
#from .models import Home, About, Profile, Category, Skills, Portfolio, Contact
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact
#from .models import Contact

# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)

# contact
class ContactAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'created_at']
  search_fields = ['name','email']
  list_per_page = 6

admin.site.register(Contact, ContactAdmin)



