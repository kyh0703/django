from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView,
)

from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"


class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # .save()
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")


class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by("first_name")
    context_object_name = "teacher_list"


class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # URL NOT a template.html
    success_url = reverse_lazy("classroom:thank_you")

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request.POST)
        return super().form_valid(form)
