from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm, LeadModelForm, SignUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login

# Create your views here.

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
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

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    success_url = reverse_lazy("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    success_url = reverse_lazy("leads:lead-list")

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads/lead_list.html", context)