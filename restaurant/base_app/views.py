from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, MenuItem, Review, Booking
from django.http import JsonResponse

# Create your views here.

def homeView(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.filter(is_available=True)[:6]  # Show only 6 items on home
    reviews = Review.objects.all()[:3]  # Show only 3 reviews on home
    context = {
        'list': categories,
        'items': menu_items,
        'review': reviews,
    }
    return render(request, 'home.html', context)

def aboutView(request):
    return render(request, 'about.html')

def menuView(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.filter(is_available=True)
    
    # Filter by category if provided
    category_id = request.GET.get('category')
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
    
    context = {
        'categories': categories,
        'menu_items': menu_items,
        'selected_category': category_id,
    }
    return render(request, 'menu.html', context)

def bookTableView(request):
    if request.method == 'POST':
        try:
            booking = Booking.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                persons=request.POST['persons'],
                date=request.POST['date'],
                time=request.POST['time'],
                special_requests=request.POST.get('special_requests', '')
            )
            messages.success(request, f'Table booked successfully for {booking.name}!')
            return redirect('book_table')
        except Exception as e:
            messages.error(request, 'Error booking table. Please try again.')
    
    return render(request, 'book_table.html')

def contactView(request):
    if request.method == 'POST':
        # Handle contact form submission
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'contact.html')