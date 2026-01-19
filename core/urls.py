from django.urls import path
from .views import book_list, borrow_book
from .views import book_list, borrow_book, return_book, loan_history
from .views import book_list, borrow_book, return_book, loan_history, add_review



urlpatterns = [
    path('', book_list, name='book_list'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
    path('history/', loan_history, name='loan_history'),
    path('review/<int:book_id>/', add_review, name='add_review'),


]