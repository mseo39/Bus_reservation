from django.shortcuts import render, redirect, get_object_or_404
from main.models  import Bus
# Create your views here.

def seat(request):

    chk_list = []
    i=1
    while i<10:
        bus_number=get_object_or_404(Bus, number=i)
        if bus_number.check==1:
            chk_list.append("disabled")
        if bus_number.check!=1:
            chk_list.append("")
        i=i+1

    return render(request,'seat.html',{'list':chk_list})

def chk(request):
    #폼 입력값 가져오기
    if request.method == 'POST':
        selected = request.POST.getlist('answer[]')

        for select in selected:
            number=get_object_or_404(Bus, number=select)
            number.check+=1
            number.save()

        return redirect('seat')

    return redirect('seat')
