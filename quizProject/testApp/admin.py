from django.contrib import admin
from testApp.models import Javamcq,Pythonmcq,Cplusmcq,Aptitudemcq

# Register your models here.

class JavamcqAdmin(admin.ModelAdmin):
    list_display=['question','opt1','opt2','opt3','opt4','correct_ans']

class PythonmcqAdmin(admin.ModelAdmin):
    list_display=['question','opt1','opt2','opt3','opt4','correct_ans']

class CplusmcqAdmin(admin.ModelAdmin):
    list_display=['question','opt1','opt2','opt3','opt4','correct_ans']

class AptitudemcqAdmin(admin.ModelAdmin):
    list_display=['question','opt1','opt2','opt3','opt4','correct_ans']

admin.site.register(Javamcq,JavamcqAdmin)
admin.site.register(Pythonmcq,PythonmcqAdmin)
admin.site.register(Cplusmcq,CplusmcqAdmin)
admin.site.register(Aptitudemcq,AptitudemcqAdmin)
