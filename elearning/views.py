from django.shortcuts import render
from .models import Program,Course,Upload,Student,Grade,New

from django.shortcuts import redirect
from .forms import ProgramForm,CourseAddForm,UpdateProfile,UploadFormFile,AddPostForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from review import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, Avg, Max, Min, Count

def programs_view(request):
    programs = Program.objects.all()

    if request.user.is_authenticated:
        return render (
            request,'program_list.html',
            {'programs': programs},
        )
    else:
        return redirect('login')

def home(request):
    context = {
        'posts': Program.objects.all()
    }
    return render(request, 'homw_generic.html', context)

def program_add(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programs')
    else:
        form = ProgramForm()

    return render (
        request, 'program_add.html', {'form': form},
    )


def program_edit(request, pk):
    program = Program.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programs')
    else:
        form = ProgramForm(instance=program)

    return render(
        request, 'program_add.html', {'form': form},
    )


def program_delete(request, pk):
    program = Program.objects.get(pk=pk)
    program.delete()

    return redirect('programs')

def program_detail(request, pk):
    program = Program.objects.get(pk=pk)
    courses = Course.objects.filter(program_id=pk)
    # credits = Course.objects.aggregate(Sum('credits'))

    paginator = Paginator(courses, 10)
    page = request.GET.get('page')

    courses = paginator.get_page(page)

    if request.user.is_authenticated:
        return render(
            request,
            'program_single.html',
            {'program': program, 'courses': courses, 'credits': credits},
        )
    else:
        return redirect('login')


###########################################################################
def course_detail(request, pk):
    course = Course.objects.get(pk = pk)
    files = Upload.objects.filter(course_id = pk)
    users = User.objects.filter(student__course_teacher__in=[course])
    grades = Grade.objects.filter(student_id=request.user.id, course_id=pk)
    teachers = Student.objects.filter(course_teacher__in=[course])

    if request.user.is_authenticated:
        return render(
            request, 'course_single.html', {'usrs': users, 'course': course, 'files': files, 'grades': grades, 'teachers': teachers, 'media_url': settings.MEDIA_ROOT},
        )
    else:
        return redirect('login')


def update_teacher(pk_t1):
    pk_t1 = int(pk_t1)
    if pk_t1 > 0:
        course = Course.objects.latest('pk')
        t1 = User.objects.get(pk=pk_t1)

        if not User.objects.filter(student__course_teacher__in=[course], pk=pk_t1).exists():
            t1.student.course_teacher.add(course)



def course_add(request, pk):
    users = User.objects.all()
    if request.method == 'POST':
        form = CourseAddForm(request.POST)
        if form.is_valid():
            form.save()
            #update_teacher(request.POST.get('user_1'))
            if request.POST.get('submit') != 'Ruaj':
                return redirect('course_add', pk=pk)
            return redirect('program_single', pk=request.POST.get('programs'))
    else:
        form = CourseAddForm(initial={'programs':Program.objects.get(pk=pk)})

    if request.user.is_authenticated:
        return render (
            request, 'course_add.html', {'form': form, 'programs': pk, 'users': users},
        )
    else:
        return redirect('login')

def course_edit(request, pk):
    users = User.objects.all()
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseAddForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('program_single', pk=request.POST.get('program'))
    else:
        form = CourseAddForm(instance=course)

    # print(form.errors)

    if request.user.is_authenticated:
        return render (
            request, 'course_add.html', {'form': form, 'program': pk, 'users': users, 'course': pk},
        )
    else:
        return redirect('login')


def course_delete(request, pk, p_pk):
    course = Course.objects.get(pk=pk)
    course.delete()

    return redirect('program_single', pk=p_pk)

#########################################################
def students_view(request):
    students = Student.objects.all()
    programs = Program.objects.all()

    if request.method == 'GET':
        p = request.GET.get('program', '')
        name = request.GET.get('name', '')
        email = request.GET.get('email', '')

        if p != '':
            students = Student.objects.filter(program=p, first_name__contains=name, email__contains=email)
        else:
            students = Student.objects.filter(first_name__contains=name, email__contains=email)

    if request.user.is_authenticated:
        return render(
            request,
            'student_list.html',
            {'students': students, 'programs': programs, 'media_url': settings.MEDIA_ROOT},
        )
    else:
        return redirect('login')

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    success = Grade.objects.filter(student=student.user).order_by('-grade')
    details = Grade.objects.filter(student=student.user, grade__gt=4).aggregate(Avg('grade'), Max('grade'), Min('grade'))

    if request.user.is_authenticated:
        return render(
            request, 'student_profile.html', {'student': student, 'success': success, 'details': details},
        )
    else:
        return redirect('login')

def user_add(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            uid = Student.objects.latest('pk').pk
            return redirect('user_edit', pk=uid)
    else:
        form = UserCreationForm()

    print(form.errors)

    if request.user.is_authenticated:
        return render(
            request, 'user_add.html', {'form': form},
        )
    else:
        return redirect('login')


def user_edit(request, pk):
    student = Student.objects.get(pk=pk)

    instance = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save(commit=False)

            courses = request.POST.getlist('course')

            is_super = request.POST.get('is_super')

            if is_super:
                usr = User.objects.get(pk=student.user.pk)
                usr.is_admin = True
                usr.is_staff = True
                usr.is_superuser = True
                usr.save()

            for c in courses:
                grade = Grade()
                usr = User.objects.get(pk=request.POST.get('user'))
                crs = Course.objects.get(pk=c)
                if not Grade.objects.filter(course=crs, student=usr).exists():
                    grade.student = usr
                    grade.grade = 0
                    grade.course = crs
                    grade.save()

            existing_courses = list(Student.objects.values_list('course', flat=True).filter(pk=pk))

            for c in existing_courses:
                if str(c) not in courses:
                    Grade.objects.filter(student=User.objects.get(pk=request.POST.get('user')), course=c).delete()

            form.save()
            return redirect('students')
    else:
        form = UpdateProfile(instance=instance,
                             initial=({'is_super': User.objects.get(pk=student.user.pk).is_superuser}))

    return render(
        request, 'user_profile_edit.html', {'form': form, 'student': student},
    )


def home_view(request):
    uploads = Upload.objects.all().order_by('-upload_time')[:5]
    programs = Program.objects.all()
    users = User.objects.all().order_by('-last_login')[:5]
    news = New.objects.all().order_by('-create_date')[:3]

    if request.user.is_authenticated:
        return render (
            request, 'home.html', {'uploads': uploads, 'programs': programs, 'users': users, 'news': news},
        )
    else:
        return redirect('login')

def handle_file_upload(request, course_id):
    course = Course.objects.get(pk = course_id)
    if request.method == 'POST':
        form = UploadFormFile(request.POST, request.FILES, {'course': course})
        if form.is_valid():
            form.save()
            return redirect('elearning/programs/course/' + str(course_id))
    else:
        form = UploadFormFile()
    return render(
        request, 'upload_file_form.html', {'form': form, 'course': course},
    )


def handle_file_edit(request, course_id, file_id):
    course = Course.objects.get(pk=course_id)
    instance = Upload.objects.get(pk=file_id)
    if request.method == 'POST':
        form = UploadFormFile(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course_id)
    else:
        form = UploadFormFile(instance=instance)

    return render (
        request, 'upload_file_form.html', {'form': form, 'course': course}
    )


def handle_file_delete(request, course_id, file_id):
    file = Upload.objects.get(pk=file_id)
    file.delete()

    return redirect('course_detail', pk=course_id)

###########################################

def post_list(request):

    posts = New.objects.all().order_by('-create_date')
    paginator = Paginator(posts, 12)

    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(
        request, 'post_list.html', {'posts': post},
    )

def post_single(request, pk):
    post = New.objects.get(pk=pk)
    posts = New.objects.all().order_by('-create_date')[:5]
    uploads = Upload.objects.all().order_by('-upload_time')[:5]

    if request.user.is_authenticated:
        return render (
            request, 'post_single.html', {'post': post, 'posts': posts, 'uploads': uploads},
        )
    else:
        return redirect('login')
def post_add(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    if request.user.is_authenticated :
        return render (
            request, 'add_new_post.html', {'form': form},
        )
    else:
        return redirect('login')

def post_edit(request, pk):
    post = New.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm(instance=post)

    if request.user.is_authenticated:
        return render (
            request, 'add_new_post.html', {'form': form},
        )
    else:
        return redirect('login')


def post_delete(request, pk):
    post = get_object_or_404(New, pk=pk)
    post.delete()

    return redirect('home')