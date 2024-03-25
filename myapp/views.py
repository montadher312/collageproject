from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.admin.views.decorators import user_passes_test
from .forms import *
from .models import *
from django.contrib import messages



# Define a custom test function
def is_admin(user):
    return user.is_authenticated and user.is_staff

# Apply the decorator to the view function
@user_passes_test(is_admin)
def ce_1(request):
    if request.method == 'POST':
        form = ComputerEngineering_1RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ce_1')
    else:
        form = ComputerEngineering_1RequestForm()

    return render(request, 'request/ce_1.html', {'form': form})

@user_passes_test(is_admin)
def ce_2(request):
    if request.method == 'POST':
        form = ComputerEngineering_2RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ce_2')
    else:
        form = ComputerEngineering_2RequestForm()

    return render(request, 'request/ce_2.html', {'form': form})
@user_passes_test(is_admin)
def ce_3(request):
    if request.method == 'POST':
        form = ComputerEngineering_3RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ce_3')
    else:
        form = ComputerEngineering_3RequestForm()

    return render(request, 'request/ce_3.html', {'form': form})
@user_passes_test(is_admin)
def ce_4(request):
    if request.method == 'POST':
        form = ComputerEngineering_4RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ce_4')
    else:
        form = ComputerEngineering_4RequestForm()

    return render(request, 'request/ce_4.html', {'form': form})
@user_passes_test(is_admin)
def ce_5(request):
    if request.method == 'POST':
        form = Cyber_security_1RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ce_5')
    else:
        form = Cyber_security_1RequestForm()

    return render(request, 'request/ce_5.html', {'form': form})
def home(request):
     return render(request, 'home.html')






def lap1(request):
 form = ComputerEngineering_1RequestForm()

 if request.method == 'POST':
        form = ComputerEngineering_1RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_1Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

 return render(request, 'lap/lap1.html', {'form': form})


def lap2(request):
    form = ComputerEngineering_2RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_2RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_2Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap2.html', {'form': form})
def lap3(request):
    form = ComputerEngineering_3RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_3RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_3Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap3.html', {'form': form})
def lap32(request):
    form = ComputerEngineering_32RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_32RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_32Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap32.html', {'form': form})

def lap4(request):
    form = ComputerEngineering_4RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_4RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_4Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap4.html', {'form': form})
def lap42(request):
    form = ComputerEngineering_42RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_42RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_42Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap42.html', {'form': form})

def less(request):
    return render(request, 'les1.html')

def less1(request):
    return render(request, 'les2.html')
def less31(request):
    return render(request, 'les31.html')
def less32(request):
    return render(request, 'les32.html')
def less41(request):
    return render(request, 'les41.html')
def less42(request):
    return render(request, 'les42.html')

def elc(request):
    return render(request, 'les/lesal.html')
def elc1(request):
    return render(request, 'les/lesal1.html')
def stage(request):
    return render(request, 'les/stage.html')
def stagecyber(request):
    return render(request, 'les/stagecyber.html')
def done_view(request):
    return render(request, 'done.html')
def les1cyber(request):
    return render(request, 'les1cyber.html')


def comp1(request):
    form = ComputerEngineering_1RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_1RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_1Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'computer/comp1.html', {'form': form})



def comp2(request):
    form = ComputerEngineering_2RequestForm()

    if request.method == 'POST':
        form = ComputerEngineering_2RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = ComputerEngineering_2Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'computer/comp2.html', {'form': form})

def lap1cyber(request):
    form = Cyber_security_1RequestForm()

    if request.method == 'POST':
        form = Cyber_security_1RequestForm(request.POST)
        if form.is_valid():
            selected_student = form.cleaned_data.get('student')
            selected_chair = form.cleaned_data.get('chair')

            # التحقق من أن الطالب لم يختار كرسيًا بعد
            existing_request = Cyber_security_1Request.objects.filter(student=selected_student).exclude(chair=None).exists()

            if existing_request:
                form.add_error('student', 'الطالب اختار كرسيًا بالفعل!')
            else:
                form.save()
                return redirect('done_view')

    return render(request, 'lap/lap1.html', {'form': form})




@user_passes_test(is_admin, login_url='/home/')
def show_requests1(request):
    # استرجاع كل الطلبات
    requests = ComputerEngineering_11Request.objects.all()
    
   
    return render(request, 'request/ce_1.html', {'requests': requests})


def accept_request1(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_11Request, pk=request_id)
    # تعديل حالة الطلب إلى "Accepted"
    request_obj.status = 'Accepted'
    request_obj.save()
    return redirect('show_requests1')

def reject_request1(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_11Request, pk=request_id)
    # تعديل حالة الطلب إلى "Rejected"
    request_obj.status = 'Rejected'
    request_obj.save()
    return redirect('show_requests1')
@user_passes_test(is_admin, login_url='/home/')
def show_requests2(request):
    # استرجاع كل الطلبات
    requests = ComputerEngineering_22Request.objects.all()
    return render(request, 'request/ce_2.html', {'requests': requests})


def accept_request2(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_22Request, pk=request_id)
    # تعديل حالة الطلب إلى "Accepted"
    request_obj.status = 'Accepted'
    request_obj.save()
    return redirect('show_requests2')

def reject_request2(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_22Request, pk=request_id)
    # تعديل حالة الطلب إلى "Rejected"
    request_obj.status = 'Rejected'
    request_obj.save()
    return redirect('show_requests2')
@user_passes_test(is_admin, login_url='/home/')
def show_requests3(request):
    # استرجاع كل الطلبات
    requests = ComputerEngineering_33Request.objects.all()
    return render(request, 'request/ce_3.html', {'requests': requests})


def accept_request3(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_33Request, pk=request_id)
    # تعديل حالة الطلب إلى "Accepted"
    request_obj.status = 'Accepted'
    request_obj.save()
    return redirect('show_requests3')

def reject_request3(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_33Request, pk=request_id)
    # تعديل حالة الطلب إلى "Rejected"
    request_obj.status = 'Rejected'
    request_obj.save()
    return redirect('show_requests3')

@user_passes_test(is_admin, login_url='/home/')
def show_requests4(request):
    # استرجاع كل الطلبات
    requests = ComputerEngineering_44Request.objects.all()
    return render(request, 'request/ce_4.html', {'requests': requests})


def accept_request4(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_44Request, pk=request_id)
    # تعديل حالة الطلب إلى "Accepted"
    request_obj.status = 'Accepted'
    request_obj.save()
    return redirect('show_requests4')

def reject_request4(request, request_id):
    # استرجاع الطلب المحدد
    request_obj = get_object_or_404(ComputerEngineering_44Request, pk=request_id)
    # تعديل حالة الطلب إلى "Rejected"
    request_obj.status = 'Rejected'
    request_obj.save()
    return redirect('show_requests4')

def delete_all_data1(request):
    if request.method == 'POST':
        # حذف جميع البيانات
        ComputerEngineering_1Request.objects.all().delete()

        # استرجاع كل الطلبات بعد الحذف
        requests = ComputerEngineering_11Request.objects.all()
        return render(request, 'request/ce_1.html', {'requests': requests})

    return render(request, 'delete/delete_all_data1.html')
def delete_all_data2(request):
    if request.method == 'POST':
        # حذف جميع البيانات
        ComputerEngineering_2Request.objects.all().delete()

        # استرجاع كل الطلبات بعد الحذف
        requests = ComputerEngineering_22Request.objects.all()
        return render(request, 'request/ce_2.html', {'requests': requests})

    return render(request, 'delete/delete_all_data2.html')
def delete_all_data3(request):
    if request.method == 'POST':
        # حذف جميع البيانات
        ComputerEngineering_3Request.objects.all().delete()

        # استرجاع كل الطلبات بعد الحذف
        requests = ComputerEngineering_33Request.objects.all()
        return render(request, 'request/ce_3.html', {'requests': requests})

    return render(request, 'delete/delete_all_data3.html')
def delete_all_data4(request):
    if request.method == 'POST':
        # حذف جميع البيانات
        ComputerEngineering_4Request.objects.all().delete()

        # استرجاع كل الطلبات بعد الحذف
        requests = ComputerEngineering_44Request.objects.all()
        return render(request, 'request/ce_4.html', {'requests': requests})

    return render(request, 'delete/delete_all_data4.html')
