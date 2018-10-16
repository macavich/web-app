from django.urls import path

from . import views

urlpatterns = [
    # ex: /portfolio/
    path('', views.index, name='index'),
    # ex: /portfolio/us-beta/
    path('<strategy_slug>/', views.portfolio_index, name='portfolio_display'),
    # ex: /portfolio/5/results/
    path('<strategy_slug>/<substrategy_slug>/', views.substrategy_index, name='substrategy_display'),
    # ex: /portfolio/5/vote/
    path('<symbol>/vote/', views.vote, name='vote'),
]
