from django.shortcuts import render, redirect
from .models import BookTable, BookLawn
from django.views.generic import (TemplateView,ListView,CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookTableForm, BookLawnForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime as dt
from datetime import datetime, date, time

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
# class CreateTable(LoginRequiredMixin, CreateView):
#     model = BookTable
#     form_class = BookTableForm
#
#     def form_valid(self, form):
#         table = form.save(commit=False)
#         form.instance.booked_by = self.request.user
#         send_mail('Village Vatiki','Hello, from Village Vatika.Your booking is confirmed','Raghu5910@outlook',['raghuram5910@gmail.com'],fail_silently=True)
#         messages.success(self.request, f'Table reserved for {self.request.user}!, you will receive confirmation mail shortly!')
#         return super(CreateTable, self).form_valid(form)

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)

        if form.is_valid():
            table = form.save(commit=False)
            table.booked_by = request.user
            timeobj = table.time
            t0=datetime.combine(date.min, timeobj) - datetime.min
            # print(type(t1))
            t1 = t0 + dt.timedelta(minutes=40)
            time1 = str(t1)
            t2 = t0 - dt.timedelta(minutes=40)
            time2 = str(t2)
            query1 = len(BookTable.objects.filter(date=table.date,booked_by = request.user))
            query2 = len(BookTable.objects.filter(date=table.date,time__lte=time1,time__gte=time2))
            print(query2)
            if query1 < 2 and query2 < 6:
                table.save()
                messages.success(request, f'Table reserved for {request.user}!, you will receive confirmation mail shortly!')
                return redirect('home:home-page')
            elif query1 >= 2:
                messages.success(request, f'You have already reserved two tables for the same date')
                return redirect('home:home-page')
            elif query2 >= 6:
                messages.success(request, f'Sorry!Tables are full!')
                return redirect('home:home-page')
    else:
        form = BookTableForm()

    return render(request,'Table/booktable_form.html',{'form':form})


class CreateLawn(LoginRequiredMixin, CreateView):
    model = BookLawn
    form_class = BookLawnForm
    template_name = 'Table/booklawn_form.html'

    def form_valid(self, form):
        table = form.save(commit=False)
        form.instance.booked_by = self.request.user
        send_mail('Village Vatiki','Hello, from Village Vatika.Your booking is confirmed','Raghu5910@outlook',['raghuram5910@gmail.com'],fail_silently=True)
        message.success(request, f'Table booked for the {self.request.user}!')
        return super(CreateLawn, self).form_valid(form)

class TableListView(LoginRequiredMixin, TemplateView):
    template_name = 'Table/booking_list.html'

    def get(self, request):

        query1 = BookTable.objects.filter(booked_by=self.request.user).order_by('time')
        context = {'bookings':query1}
        return render(request, self.template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AdminTableList(request):
    query1 = BookTable.objects.filter(date__gte=datetime.date.today()).order_by('date')
    return render(request,'Table/tables.html',{'query1':query1})
