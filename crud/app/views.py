from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('student_list')
            return redirect('/?status=added') 
    return render(request, 'index.html', {'form': form, 'students': students})

    
def student_delete(request, student_id):
    student = Student.objects.get(student_id=student_id)
    student.delete()
    return redirect('/?status=deleted')

def student_edit(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student = Student.objects.get(student_id=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/?status=edited')  
    return redirect('student_list')  