from django.views import generic

from prototype.models import Student, Je


class StudentListView(generic.ListView):
    template_name = 'prototype/student_list.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """
        Return all students
        """
        return Student.objects.all()


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'prototype/student_detail.html'


class JeListView(generic.ListView):
    template_name = 'prototype/je_list.html'
    context_object_name = 'je_list'

    def get_queryset(self):
        """
        Return all Je
        """
        return Je.objects.all()


class JeDetailView(generic.DetailView):
    model = Je
    template_name = 'prototype/je_detail.html'
