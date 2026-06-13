"""evaluator/urls.py — App ke routes"""

from django.urls import path
from .views import EvaluateView, HistoryListView, HistoryDetailView, LeaderboardView

urlpatterns = [
    path('evaluate/', EvaluateView.as_view(), name='evaluate'),          # POST
    path('history/', HistoryListView.as_view(), name='history-list'),    # GET
    path('history/<int:pk>/', HistoryDetailView.as_view(), name='history-detail'),  # GET
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'), # GET
]
