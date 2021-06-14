from django.urls import path,include
from quotes.api.views import QuoteDetailAPIview,QuoteListCreateAPIView
urlpatterns = [
    path('quotes',QuoteListCreateAPIView.as_view(), name = "quote-list"),
    path('quotes/<int:pk>',QuoteListCreateAPIView.as_view(), name = "quote-detail")
    # path('api/',include('quotes.api.urls'))
]
