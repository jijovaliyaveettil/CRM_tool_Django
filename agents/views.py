from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from leads.models import Agent, Lead
from .forms import AgentForm

class AgentListView(LoginRequiredMixin, ListView):
    # model = Agent
    template_name = "agents/agent_list.html"
    context_object_name = "agents"
    queryset = Agent.objects.all()
    # success_url = reverse_lazy('agents:agent-list')


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentForm
    success_url = reverse_lazy('agents:agent-list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super().form_valid(form)

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    queryset = Agent.objects.all()

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentForm
    queryset = Agent.objects.all()
    success_url = reverse_lazy('agents:agent-list')

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()
    success_url = reverse_lazy('agents:agent-list')
# Create your views here.
