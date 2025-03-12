from django.shortcuts import render
from .ai import get_ai_response
from .models import WW2Event, TatneftHistory
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('q', '')
    ww2_results = WW2Event.objects.filter(
        Q(description__icontains=query) | Q(category__icontains=query)
    )
    tatneft_results = TatneftHistory.objects.filter(
        Q(event__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'search.html', {
        'ww2_results': ww2_results,
        'tatneft_results': tatneft_results,
        'query': query
    })

def chat_bot(request):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = get_ai_response(question)
        return render(request, "chat.html", {"question": question, "answer": answer})
    return render(request, "chat.html")