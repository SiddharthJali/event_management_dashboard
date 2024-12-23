from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Attendee, Task
from .forms import EventForm, AttendeeForm, TaskForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def event_create_edit(request, pk=None):
    if pk:
        event = get_object_or_404(Event, pk=pk)
        form_title = 'Edit Event'
    else:
        event = None
        form_title = 'Create Event'

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            print("Form is valid and saved.")
            return redirect('event_list')
        else:
            print("Form is not valid.")
    else:
        form = EventForm(instance=event)

    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.add_input(Submit('submit', 'Save'))

    return render(request, 'events/form.html', {
        'form': form,
        'form_title': form_title
    })

def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'events/attendees.html', {'attendees': attendees})

def attendee_create_edit(request, pk=None):
    if pk:
        attendee = get_object_or_404(Attendee, pk=pk)
        form_title = 'Edit Attendee'
    else:
        attendee = None
        form_title = 'Create Attendee'

    if request.method == 'POST':
        form = AttendeeForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            print("Form is valid and saved.")
            return redirect('attendee_list')
        else:
            print("Form is not valid.")
    else:
        form = AttendeeForm(instance=attendee)

    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.add_input(Submit('submit', 'Save'))

    return render(request, 'events/form.html', {
        'form': form,
        'form_title': form_title
    })

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'events/tasks.html', {'tasks': tasks})

def task_create_edit(request, pk=None):
    if pk:
        task = get_object_or_404(Task, pk=pk)
        form_title = 'Edit Task'
    else:
        task = None
        form_title = 'Create Task'

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("Form is valid and saved.")
            return redirect('task_list')
        else:
            print("Form is not valid.")
    else:
        form = TaskForm(instance=task)

    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.add_input(Submit('submit', 'Save'))

    return render(request, 'events/form.html', {
        'form': form,
        'form_title': form_title
    })

def dashboard(request):
    total_events = Event.objects.count()
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    attendees_doing_tasks = Attendee.objects.filter(task__status__in=['In Progress', 'Pending']).distinct().count()
    attendees_free = Attendee.objects.filter(task__status='Completed').distinct().count() + Attendee.objects.filter(task__isnull=True).distinct().count()

    return render(request, 'events/dashboard.html', {
        'total_events': total_events,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress': progress,
        'attendees_doing_tasks': attendees_doing_tasks,
        'attendees_free': attendees_free,
    })

def event_confirm_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/confirm_delete.html', {
        'model_name': 'Event', 'redirect_url': 'event_list'
    })

def attendee_confirm_delete(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        attendee.delete()
        return redirect('attendee_list')
    return render(request, 'events/confirm_delete.html', {
        'model_name': 'Attendee', 'redirect_url': 'attendee_list'
    })

def task_confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'events/confirm_delete.html', {
        'model_name': 'Task', 'redirect_url': 'task_list'
    })
