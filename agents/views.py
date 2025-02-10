from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from leads.models import Agent, Lead
from .forms import AgentModelForm
from .mixins import LoginandOrgMixin
from django.core.mail import send_mail
import random

def send_welcome_email(user):
    subject = 'Welcome to CRM Tool'
    message = f'Hello {user.username},\n\nWelcome to our CRM Tool. We are excited to have you on board.\n\nBest regards,\nCRM Team'
    from_email = 'support@crm.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

class AgentListView(LoginandOrgMixin, ListView):
    # model = Agent
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        queryset = Agent.objects.filter(organisation=organisation)
        return queryset

class AgentCreateView(LoginandOrgMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(100000, 999999)}")
        user.save()

        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_welcome_email(user)
        return super().form_valid(form)

class AgentDetailView(LoginandOrgMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    queryset = Agent.objects.all()

class AgentUpdateView(LoginandOrgMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    queryset = Agent.objects.all()
    success_url = reverse_lazy('agents:agent-list')

class AgentDeleteView(LoginandOrgMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()
    success_url = reverse_lazy('agents:agent-list')
# Create your views here.
