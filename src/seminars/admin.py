from django.contrib import admin

from .models import (ClassMaterial, Instructor, SeminarType, SeminarLocation,
                     Seminar, SeminarTypePrerequisite)


class PrerequisiteInline(admin.StackedInline):
    model = SeminarTypePrerequisite
    fk_name = 'from_seminartype'


class SeminarTypeAdmin(admin.ModelAdmin):
    inlines = (PrerequisiteInline,)


admin.site.register(ClassMaterial)
admin.site.register(Instructor)
admin.site.register(SeminarType, SeminarTypeAdmin)
admin.site.register(SeminarLocation)
admin.site.register(Seminar)
