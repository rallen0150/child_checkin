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
    success_url = reverse_lazy('index_view')

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('access_level', )
    success_url = reverse_lazy('index_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["children"] = Child.objects.all()
        return context

    # To find the child's information
    def post(self, request):
        print(request.POST)
        pin = request.POST['pincode']
        child_pin = Child.objects.get(pincode=pin)
        return HttpResponseRedirect("http://localhost:8000/child/{}/".format(child_pin.id))

class ChildCreateView(CreateView):
    model = Child
    fields = ('first_name', 'last_name', 'parent', 'picture')
    success_url = reverse_lazy('employee_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.parent = self.request.user
        instance.pincode = ''
        for num in range(4):
            instance.pincode += choice(digits)
        return super().form_valid(form)

class ChildDetailView(DetailView):
    model = Child

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child"] = Child.objects.all()
        return context

class TimeCreateView(CreateView):
    model = Time
    fields = ('checkin', )
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.child = Child.objects.get(id=self.kwargs['pk'])
        if instance.checkin:
            return super().form_valid(form)
        return super().form_valid(form)

class TimeUpdateView(UpdateView):
    model = Time
    fields = ('checkin', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('checkin_success_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        if not instance.checkin:
            instance.checkout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return super().form_valid(form)
        return super().form_valid(form)

class EmployeeListView(ListView):
    model = Child

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child_list"] = Child.objects.all()
        return context

class SchoolDetailView(TemplateView):
    template_name = 'class.html'
    # model = Time

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["class_list"] = Time.objects.all()
        return context

class CheckinSuccessView(TemplateView):
    template_name = ('checkin_app/success.html')
    model = Time

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = Time.objects.get(id=self.kwargs['pk'])
        return context
