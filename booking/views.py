from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TableBooking

def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
        TableBooking.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            message=message
        )
        
        messages.success(request, 'Your table booking request has been submitted successfully!')
        return redirect('booking:book_table')
    
    return render(request, 'booking/book_table.html')
