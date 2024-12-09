from django.shortcuts import render, HttpResponse
from googletrans import Translator  

def home(request):
    translation = None
    if request.method == "POST":
        text = request.POST.get("translate", "")
        language = request.POST.get("language", "")
        
        if not text or not language:
            return HttpResponse("Oba pola (tekst i język) muszą być wypełnione.", status=400)

        try:
            translator = Translator()
            translation = translator.translate(text, dest=language).text
        except Exception as e:
            return HttpResponse(f"Błąd: {e}", status=500)

    return render(request, "main/index.html", {"translation": translation})
