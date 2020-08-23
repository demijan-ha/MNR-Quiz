from django.shortcuts import render

# Create your views here.
def Index(request):
    num_lemmas = Lemma.objects.all().count()
    num_lemmas_approved = Lemma.objects.filter(approved=True).count()
    prcnt_done = round((num_lemmas_approved / num_lemmas) * 100, 1)
    active_user = request.user

    context = {
        'num_lemmas': num_lemmas,
        'num_lemmas_approved': num_lemmas_approved,
        'prcnt_done': prcnt_done,
        'active_user': active_user
    }

    return render(request, 'dictionary/index.html', context=context)