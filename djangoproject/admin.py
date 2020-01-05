from django.contrib import admin
from .models import Post,Question,Answer,File_Document,Topic,Admin_instructor_Add,Teacher_Program
admin.site.register(Post)

admin.site.register(Question)

admin.site.register(Answer)


admin.site.register(Admin_instructor_Add)

admin.site.register(Teacher_Program)