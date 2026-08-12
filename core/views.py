from django.shortcuts import render


def home(request):
    """Exibe a página institucional do sistema."""
    return render(request, "home.html")
