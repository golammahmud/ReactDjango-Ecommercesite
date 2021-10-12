from django.contrib import admin
from testapi.models import Student



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     list_display = ('id','name','age','address','created_at')
     list_display_links = ('id','name')

