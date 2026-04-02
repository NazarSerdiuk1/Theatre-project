# Theatre API

## Description
Theatre API is a RESTful API for managing theatrical performances, actors, genres, halls, reservations, and tickets. The project is built using Django REST Framework and PostgreSQL. Docker support is also included for easy deployment.

## Technology Stack
- Python 
- Django 5
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose

## Installation and Setup

### Clone the Repository
```sh
git clone https://github.com/NazarSerdiuk1/Theatre-project.git
cd Theatre-project
```

### Run with Docker
```sh
docker-compose up --build
```
The API will be available at `http://localhost:8000/`.

### Run without Docker
1. Set up a virtual environment and install dependencies:
```sh
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
2. Create a PostgreSQL database and configure `DATABASES` in `settings.py`.
3. Apply migrations:
```sh
python manage.py migrate
```
4. Create a superuser (optional):
```sh
python manage.py createsuperuser
```
5. Start the server:
```sh
python manage.py runserver
```

## Data Models

### Play
- `title` – title
- `description` – description

### Actor
- `first_name` – first name
- `last_name` – last name

### Genre
- `name` – genre name

### TheatreHall
- `name` – name
- `rows` – number of rows
- `seats_in_row` – number of seats per row

### Performance
- `play` – reference to a play
- `theatre_hall` – reference to a hall
- `show_time` – show time

### Reservation
- `user` – user
- `created_at` – creation date

### Ticket
- `row` – row number
- `seat` – seat number
- `performance` – performance reference
- `reservation` – reservation reference

## API Endpoints

| HTTP Method | Endpoint | Description |
|------------|----------|-------------|
| GET, POST | `/plays/` | Retrieve list of plays, create a play |
| GET, PATCH, DELETE | `/plays/{id}/` | Retrieve, update, delete a play |
| PATCH | `/plays/{id}/mark_as_played/` | Mark a play as performed |
| GET, POST | `/actors/` | Retrieve list of actors, create an actor |
| GET, PATCH, DELETE | `/actors/{id}/` | Retrieve, update, delete an actor |
| GET, POST | `/genres/` | Retrieve list of genres, create a genre |
| GET, PATCH, DELETE | `/genres/{id}/` | Retrieve, update, delete a genre |
| GET, POST | `/theatre_halls/` | Retrieve list of halls, create a hall |
| GET, PATCH, DELETE | `/theatre_halls/{id}/` | Retrieve, update, delete a hall |
| GET, POST | `/performances/` | Retrieve list of performances, create a performance |
| GET, PATCH, DELETE | `/performances/{id}/` | Retrieve, update, delete a performance |
| GET, POST | `/reservations/` | Retrieve list of reservations, create a reservation |
| GET, DELETE | `/reservations/{id}/` | Retrieve, delete a reservation |
| GET, POST | `/tickets/` | Retrieve list of tickets, create a ticket |
| GET, DELETE | `/tickets/{id}/` | Retrieve, delete a ticket |

