from django.shortcuts import render, redirect
from .models import Resume, Section, ResumeTemplate
from .forms import ResumeForm, SectionForm
from django.contrib.auth.decorators import login_required

@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('edit_resume', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'resumes/create_resume.html', {'form': form})

@login_required
def edit_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    sections = Section.objects.filter(resume=resume)
    return render(request, 'resumes/edit_resume.html', {'resume': resume, 'sections': sections})

@login_required
def add_section(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.resume = resume
            section.save()
            return redirect('edit_resume', resume_id=resume.id)
    else:
        form = SectionForm()
    return render(request, 'resumes/add_section.html', {'form': form})

@login_required
def delete_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    resume.delete()
    return redirect('list_resumes')

@login_required
def list_resumes(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resumes/list_resumes.html', {'resumes': resumes})