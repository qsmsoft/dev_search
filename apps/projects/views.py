from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import search_projects, paginate_projects
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm


# Create your views here.


def projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginate_projects(request, projects, 6)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_obj
        review.owner = request.user.profile
        review.save()

        # update project votecount
        project_obj.get_vote_count

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=project_obj.id)

    context = {
        'project': project_obj,
        'tags': tags,
        'form': form,
    }
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')

    context = {
        'form': form,
        'project': project,
    }
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-template.html', context)
