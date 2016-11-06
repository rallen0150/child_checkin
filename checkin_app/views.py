from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import datetime

from random import choice
from string import digits
from checkin_app.models import Child, Profile, Time


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["children"] = Child.objects.all()
        return context

    def post(self, request):
        print(request.POST)
        pin = request.POST['pin_number']
        child_pin = Child.objects.get(pin_number=pin)

        return HttpResponseRedirect("http://localhost:8000/child/{}/".format(child_pin.id))

class ChildCreateView(CreateView):
    model = Child
    fields = ('first_name', 'last_name', 'parent')
    success_url = reverse_lazy('employee_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.parent = self.request.user
        instance.pin_number = ''
        for num in range(4):
            instance.pin_number += choice(digits)
        return super().form_valid(form)

class ChildDetailView(DetailView):
    model = Child

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child"] = Child.objects.all()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["time_list"] = Time.objects.all()
    #     return context

class TimeCreateView(CreateView):
    model = Time
    fields = ('checkin', )
    success_url = reverse_lazy('employee_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.child = Child.objects.get(id=self.kwargs['pk'])
        if instance.checkin:
            return super().form_valid(form)
        return super().form_valid(form)

class TimeUpdateView(UpdateView):
    model = Time
    fields = ('checkin', )
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        if not instance.checkin:
            instance.checkout_time = datetime.now()
            return super().form_valid(form)
        return super().form_valid(form)


# class ChildUpdateView(UpdateView):
#     model = Time
#     fields = ('checkin', )
#     success_url = reverse_lazy('index_view')
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         if instance.checkin:
#             instance.checkin_time = datetime.now()
#         else:
#             instance.checkout_time = datetime.now()
#         return super().form_valid(form)

class EmployeeListView(ListView):
    model = Child

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child_list"] = Child.objects.all()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_list'] = Profile.objects.all()
    #     return context

# class SchoolDetailView(TemplateView):
#     template_name = 'class.html'
#     model = Time
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["class_list"] = Time.objects.all()
#         return context
