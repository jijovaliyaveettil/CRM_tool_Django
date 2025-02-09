from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm, LeadModelForm, SignUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)

        queryset = Lead.objects.filter(agent__user=user)
        return queryset

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)

        queryset = Lead.objects.filter(agent__user=user)
        return queryset

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/leads_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("leads:lead-list")
    def form_valid(self, form):
        send_mail(
            subject="Lead Created",
            message="You have successfully created a lead.",
            from_email="support@crm.com",
            recipient_list=["support2@crm.com"],
        )
        return super().form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)

        queryset = Lead.objects.filter(agent__user=user)
        return queryset

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)

        queryset = Lead.objects.filter(agent__user=user)
        return queryset

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

def home(request):
    return render(request, "home.html")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads/lead_list.html", context)