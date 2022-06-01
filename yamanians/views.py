from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class YamanianListView(ListView):
    model = models.Yamanian

class YamanianDetailView(DetailView):
    model = models.Yamanian

class YamanianUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Yamanian
    fields = [
        "full_name",
        "anime",
        "age",
        "about"
    ]
    success_url ="/yamanians"

class YamanianDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Yamanian
    fields = "__all__"
    success_url = "/yamanians"

class YamanianCreateView(LoginRequiredMixin ,CreateView):
    model = models.Yamanian
    fields = ["full_name", "age", "anime", "about"]
    success_url = "/yamanians"

    def form_valid(self, form):
        form.instance.nickname = self.request.user
        return super().form_valid(form)

    

class AnimeListView(ListView):
    model = models.Anime

class AnimeDetailView(DetailView):
    model = models.Anime

class AnimeCreateView(LoginRequiredMixin, CreateView):
    model = models.Anime
    fields = "__all__"
    success_url = "/anime"

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ["title","anime","text"]
    success_url = "/anime"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registeration/register.html"
    success_url = "/accounts/login/?next=/yamanians"
