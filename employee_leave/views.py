from django.shortcuts import render, redirect
from .models import Employee, Leave
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Count
@login_required(login_url="/login")
def homepage(request):
    if request.user.is_superuser:
        employees = Employee.objects.all()
        all_leaves = Leave.objects.all()

        number = employees.count()
        leaves = all_leaves.filter(leave_date=datetime.date.today())
        total_leaves = all_leaves.filter(leave_date__month=datetime.datetime.now().month)
        leaves_pending = all_leaves.filter(leave_date=datetime.date.today(), status='pending').count()

        today_leaves = leaves.count()
        total_month_leave = total_leaves.values('leave_date').annotate(Count('leave_date'))
        total_leave_type_count = total_leaves.values('leave_type').annotate(Count('leave_type'))
        return render(request, 'index.html', {'employees':employees, 'number':number, 'today_leaves':today_leaves, 'leaves_pending':leaves_pending, 'total_leave_type':total_leave_type_count, 'total_month_leave':total_month_leave})
    else:
        employees = Employee.objects.filter(user=request.user)
        all_leaves = Leave.objects.filter(employee=request.user)


        return render(request, 'index.html', {})

def employee(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request, 'employee.html', context)

@login_required(login_url="/login")
def leave(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        leave_date = request.POST.get('leaving_date')
        returning_date = request.POST.get('returning_date')
        comment = request.POST.get('comment')
        if request.user.is_anonymous:
            return redirect('home')
        else:
            # employees = Employee.objects.get(user=request.user)
            leave_obj = Leave(employee=request.user, leave_type=leave_type, leave_date=leave_date, return_date=returning_date, comment=comment)
            leave_obj.save()
            return redirect('home')
    else:
        applied_leave = Leave.objects.filter(employee=request.user)
        return render(request, 'leave.html', {'leaves':applied_leave})

