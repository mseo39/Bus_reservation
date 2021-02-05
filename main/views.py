from django.shortcuts import render, redirect, get_object_or_404
from main.models  import Bus
# Create your views here.

#---------예매
# def seat(request):

#     if request.method == 'POST':
#         date=request.POST['date']
#         chk_list = []
#         i=1
#         while i<10:
#             bus_number=get_object_or_404(Bus, number=i, date=date)
#             if bus_number.check==1:
#                 chk_list.append("disabled")
#             if bus_number.check!=1:
#                 chk_list.append("")
#             i=i+1
#         return render(request,'seat.html',{'list':chk_list, 'date':date})
#     return render(request,'seat.html')

#------------------예매 취소

# def seat_cancel(request):

#     chk_list = []
#     i=1
#     while i<10:
#         bus_number=get_object_or_404(Bus, number=i)
#         if bus_number.check==1:
#             chk_list.append("")
#         if bus_number.check!=1:
#             chk_list.append("disabled")
#         i=i+1

#     return render(request,'seat_cancel.html',{'list':chk_list})

def chk(request):
    #폼 입력값 가져오기
    if request.method == 'POST':
        selected = request.POST.getlist('answer[]')
        date=request.POST['date']
        for select in selected:
            number=get_object_or_404(Bus, number=select, date=date)
            number.check+=1
            number.save()

        return redirect('date')

    return redirect('date')

def chk_cancel(request):
    #폼 입력값 가져오기
    if request.method == 'POST':
        selected = request.POST.getlist('answer[]')
        date=request.POST['date']

        for select in selected:
            number=get_object_or_404(Bus, number=select, date=date)
            number.check-=1
            number.save()

        return redirect('date')

    return redirect('date')

#-------------------날짜별

def select_date(request):
    #폼 입력값 가져오기
    date=request.POST['date']

    if Bus.objects.filter(date__contains='{}'.format(date)).count()>0:
        date=request.POST['date']
        chk_list = []
        i=1
        while i<10:
            bus_number=get_object_or_404(Bus, number=i, date=date)
            if bus_number.check==1:
                chk_list.append("disabled")
            if bus_number.check!=1:
                chk_list.append("")
            i=i+1
        return render(request,'seat.html',{'list':chk_list, 'date':date})

    else:
        i=1
        while i<10:
            bus=Bus()
            bus.number=i
            bus.check=0
            bus.date=date
            bus.save()
            i=i+1
        
        return render(request,'seat.html',{'date':date})

def cancel_date(request):
    #폼 입력값 가져오기
    date=request.POST['date']

    chk_list = []
    i=1
    while i<10:
        bus_number=get_object_or_404(Bus, number=i, date=date)
        if bus_number.check==1:
            chk_list.append("")
        if bus_number.check!=1:
            chk_list.append("disabled")
        i=i+1

    return render(request,'seat_cancel.html',{'list':chk_list, 'date':date})

def date(request):

    return render(request,'date.html')