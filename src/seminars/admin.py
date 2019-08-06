from django.contrib import admin

from .models import (ClassMaterial, Instructor, SeminarType, SeminarLocation,
                     Seminar)


admin.site.register(ClassMaterial)
admin.site.register(Instructor)
admin.site.register(SeminarType)
admin.site.register(SeminarLocation)
admin.site.register(Seminar)
