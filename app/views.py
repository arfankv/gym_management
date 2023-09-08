import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from django.shortcuts import render, redirect

from app.forms import TrainerForm, CustomerForm
from app.models import Login, Attendance
import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin_panel(request):
    logins = Login.objects.all()
    return render(request, 'admin_panel.html', {'logins': logins})

def trainer_register(request):
    login_form = CustomerForm()
    if request.method == 'POST':
        login_form = CustomerForm(request.POST, request.FILES)
        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_trainer = True
            user.save()
            messages.info(request, 'register successfully')
            return  redirect('trainer_panel')
    return render(request, 'trainer_register.html', {'login_form': login_form})


def trainer_panel(request):
    return render(request, 'trainer_panel.html')


def trainer_view(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request, 'trainer_view.html', {'data': data})


def trainer_update(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        form=CustomerForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('trainer_view')
    else:
        form = CustomerForm(instance=data)
    return render(request, 'trainer_update.html', {'form': form})


def trainer_delete(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('trainer_view')
    else:
        return redirect('trainer_view')


def customer_register(request):
    login_form = CustomerForm()
    if request.method == 'POST':
        login_form = CustomerForm(request.POST, request.FILES)

        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_customer = True
            user.save()
            messages.info(request, 'register successfully')
            return redirect('customer_panel')
    return render(request, 'customer_register.html', {'login_form': login_form})


def customer_panel(request):
    data = Login.objects.filter(is_customer=True)

    context={
        'data':data,
    }
    return render(request, 'customer_panel.html',context)


def customer_view(request):
    data = Login.objects.filter(is_customer=True)
    return render(request, 'customer_view.html', {'data': data})


def customer_update(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_view')
    else:
        form = CustomerForm(instance=data)
    return render(request, 'customer_update.html', {'form': form})


def customer_delete(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('customer_view')
    else:
        return redirect('customer_view')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_panel')
            elif user.is_trainer:
                return redirect('trainer_panel')
            elif user.is_customer:
                return redirect('customer_panel')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')


def trainer_view_trainer(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request, 'trainer_view_trainer.html', {'data': data})


def customer_view_customer(request):
    data = Login.objects.filter(is_customer=True)
    return render(request, 'customer_view_customer.html', {'data': data})


def add_attendance(request):
    customer = Login.objects.filter(is_customer=True)
    return render(request, 'customer_list.html', {'customer': customer})


now = datetime.datetime.now()

def mark(request, id):
    user = Login.objects.get(id=id)
    att = Attendance.objects.filter(name=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, 'today attendance already marked')
        return redirect('add_attendance')
    else:
        if request.method =='POST':
            attndc = request.POST.get('attendance')
            Attendance(name=user, date=datetime.date.today(), attendance=attndc).save()
            return redirect('add_attendance')
        return render(request, 'mark_attendance.html')


def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'view_attendance.html', {'attendance': attendance})


def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendance': attendance,
        'date': date
    }
    return render(request, 'day_attendance.html', context)


def view_attendance_user(request):

    data = Attendance.objects.filter
    return render(request, 'view_attendance_user.html', {'data': data})


def log_out_view(request):
    logout(request)
    return redirect('home')


def profile(request):
    data = Login.objects.filter(username=request.user)
    return render(request, 'profile.html', {'data': data})

