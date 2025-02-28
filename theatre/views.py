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
        play = self.get_object()  # Get Play object by its pk
        play.status = 'played'  # Example of a status change
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

class PlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing plays.

    - Allows creating, updating, deleting, and retrieving plays.
    - Additional `mark_as_played` method marks a play as performed.
    """

    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    @action(detail=True, methods=["patch"])
    def mark_as_played(self, request, pk=None):
        """
        Marks a play as performed.

        **Request parameters**:
        - **pk** (int): ID of the play.

        **Response**:
        - `200 OK`: Successfully marked as performed.
        - `404 Not Found`: If the play does not exist.
        """
        play = self.get_object()
        play.status = "played"
        play.save()
        return Response({"message": "Play marked as played."}, status=status.HTTP_200_OK)
