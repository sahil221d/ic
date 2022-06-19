
from django.contrib import admin


from .models import Fort,Food, musicali,painting,PerfArts, freedomar, textile

# Register your models here.
@admin.register(Fort)
class fort(admin.ModelAdmin):
    list_display = ['id','title','description','fort_image']

@admin.register(Food)
class food(admin.ModelAdmin):
    list_display = ['id','title','description','food_image']

@admin.register(painting)
class food(admin.ModelAdmin):
    list_display = ['id','title','description','selling_price', 'category','product_image']

@admin.register(PerfArts)
class fort(admin.ModelAdmin):
    list_display = ['id','title','description','pa_image']

@admin.register(freedomar)
class food(admin.ModelAdmin):
    list_display = ['id','title','description', 'category','fr_image']

@admin.register(musicali)
class food(admin.ModelAdmin):
    list_display = ['id','title','description', 'category','instru_image']

@admin.register(textile)
class food(admin.ModelAdmin):
    list_display = ['id','title','description', 'category','image']