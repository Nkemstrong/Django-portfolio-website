from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Project, Skill, Profile
from .forms import ContactForm


def home(request):

    profile = Profile.objects.first()

    return render(
        request,
        "portfolio/home.html",
        {"profile": profile},
    )


def about(request):

    profile = Profile.objects.first()

    return render(
        request,
        "portfolio/about.html",
        {"profile": profile},
    )


def skills(request):

    skills = Skill.objects.all()

    return render(
        request,
        "portfolio/skills.html",
        {"skills": skills},
    )


def projects(request):

    projects = Project.objects.all().order_by("-created")

    return render(
        request,
        "portfolio/projects.html",
        {"projects": projects},
    )


def contact(request):

    profile = Profile.objects.first()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            data = form.cleaned_data

            send_mail(
                subject=f"Portfolio Contact: {data['subject']}",

                message=f"""
You have received a new message from your portfolio website.

Name: {data['name']}

Email: {data['email']}

Subject: {data['subject']}

Message:

{data['message']}
""",

                from_email=settings.DEFAULT_FROM_EMAIL,

                recipient_list=[
                    "nkemstrong223@gmail.com",
                ],

                fail_silently=False,
            )

            messages.success(
                request,
                "✅ Thank you! Your message has been sent successfully."
            )

            form = ContactForm()

    else:

        form = ContactForm()

    return render(
        request,
        "portfolio/contact.html",
        {
            "profile": profile,
            "form": form,
        },
    )