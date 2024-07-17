from django.shortcuts import render, get_object_or_404, redirect
from .models import HotelRoom, Booking
from .forms import BookingForm, HotelRoomForm


def room_list(request):
    return render(
        request,
        'booking_app/main_page.html',
        context={
            'rooms': HotelRoom.objects.all()
        }
    )


def detail_information(request, slug):
    room = get_object_or_404(HotelRoom, slug=slug)
    return render(
        request,
        'booking_app/detail_information.html',
        context={
            'room': room
        }
    )


def booking_view(request, slug):
    room = get_object_or_404(HotelRoom, slug=slug)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel_room = room
            booking.save()
            booking.user.add(request.user)
            return redirect('success')
    else:
        form = BookingForm()

    return render(
        request,
        'booking_app/booking.html',
        context={
            'room': room,
            'form': form
        }
    )


def success(request):
    return render(
        request,
        'booking_app/succes_page.html',
    )


def profile(request):
    bookings = request.user.booking.all()
    return render(
        request,
        'booking_app/Profile.html',
        context={
            'bookings': bookings
        }
    )


def delete_room(request, slug):
    room = get_object_or_404(HotelRoom, slug=slug)
    room.delete()
    return redirect('list_of_rooms')


def edit_room(request, slug):
    room = get_object_or_404(HotelRoom, slug=slug)
    if request.method == 'POST':
        form = HotelRoomForm(request.POST, instance=room)
        # Объясняя простым языком instance = заполняет форму текущими значениями
        if form.is_valid():
            form.save()
            return redirect('list_of_rooms')
    else:
        form = HotelRoomForm(instance=room)
    return render(
        request,
        'booking_app/edit_room.html',
        context={
            'form': form,
            'room': room
        }
    )


def create_room(request):
    if request.method == "POST":
        form = HotelRoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            if 'image' in request.FILES:
                room.image = request.FILES['image']
            room.save()
            return redirect('list_of_rooms')
    else:
        form = HotelRoomForm()
    return render(
        request,
        'booking_app/create_room.html',
        context={
            'form': form,
        }
    )


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('list_of_rooms')
    return render(
        request,
        'booking_app/cancel_booking.html',
        context={
            'booking': booking
        }
    )
