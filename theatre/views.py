from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Play, Actor, Genre, TheatreHall, Performance, Reservation, Ticket
from .serializers import (
    PlaySerializer, ActorSerializer, GenreSerializer,
    TheatreHallSerializer, PerformanceSerializer,
    ReservationSerializer, TicketSerializer
)

class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    @action(detail=True, methods=['patch'])
    def mark_as_played(self, request, pk=None):
        play = self.get_object()  # Получаем объект Play по его pk
        play.status = 'played'  # Пример изменения статуса
        play.save()
        return Response({"message": "Play marked as played."}, status=status.HTTP_200_OK)

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
