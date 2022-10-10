from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy
# Create your views here.
from classroom.forms import ContactForm
from classroom.models import Teacher


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    template_name = 'classroom/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    # django looks for a template called classroom/teacher_form.html
    # .save() is called automatically
    # A new instance of the model is created and saved to the database
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    # model.list_html
    model = Teacher
    queryset = Teacher.objects.order_by('last_name')

    context_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    # model.detail_html
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'age', 'subject']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView(DeleteView):
    # Form-->Confirm delete button for teacher
    # default template name
    # model_confirm_delete.html

    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:teacher_list')
