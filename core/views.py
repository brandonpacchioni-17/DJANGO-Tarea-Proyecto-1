from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Loan


def book_list(request):
    books = Book.objects.all()

    books_with_status = []
    for book in books:
        active_loan = Loan.objects.filter(
            book=book,
            return_date__isnull=True
        ).first()

        books_with_status.append({
            'book': book,
            'loan': active_loan
        })

    return render(request, 'core/book_list.html', {
        'books_with_status': books_with_status
    })




@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if Loan.objects.filter(book=book, return_date__isnull=True).exists():
        messages.error(request, "Este libro ya está prestado")
        return redirect('book_list')

    Loan.objects.create(
        book=book,
        user=request.user,
        loan_date=timezone.now()
    )

    messages.success(request, "Libro prestado correctamente")
    return redirect('book_list')


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    loan = Loan.objects.filter(book=book, return_date__isnull=True).first()
    if loan:
        loan.return_date = timezone.now()
        loan.save()
        messages.success(request, "Libro devuelto correctamente")

    return redirect('book_list')




@login_required
def loan_history(request):
    loans = Loan.objects.filter(user=request.user).order_by('-loan_date')
    return render(request, 'core/loan_history.html', {'loans': loans})
