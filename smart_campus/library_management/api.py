from ninja import NinjaAPI
from .models import books_to_be_bought, Inventory, Books
from .schemas import (
    BuyingSchema,
    GetBudget,
    BoughtSchema,
    DeleteBookSchema,
    BookCountSchema,
    UpdateStatusSchema
)
from django.http import JsonResponse


app = NinjaAPI(urls_namespace="library_api")