from django.shortcuts import render
from ceasers.ceaser import ceaseren, ceaserdec


def options(request):
    return render(request, 'ceasers/options.html')


def encrypt(request):
    if request.method == 'POST':
        flag = 1

        StringIn = str(request.POST.get('String'))
        key = int(request.POST.get('key'))
        Encrypt = ceaseren(StringIn, key)
        return render(request, 'ceasers/ceaser.html',
                      {"String": StringIn, "key": key, "flag": flag, "Encrypt": Encrypt})


    else:
        flag = 0
        StringIn = ""
        key = ""
        return render(request, 'ceasers/ceaser.html', {"String": StringIn, "key": key, "flag": flag})


def decrypt(request):
    if request.method == 'POST':
        flag = 1
        StringIn = str(request.POST.get('String'))
        key = int(request.POST.get('key'))
        Encrypt = ceaserdec(StringIn, key)
        return render(request, 'ceasers/ceaserde.html',
                      {"String": StringIn, "key": key, "flag": flag, "Encrypt": Encrypt})


    else:
        flag = 0
        StringIn = ""
        key = ""
        return render(request, 'ceasers/ceaserde.html', {"String": StringIn, "key": key, "flag": flag})
