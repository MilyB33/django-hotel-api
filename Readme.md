# Django hotel room booking API

A simple Django API app for reserving hotel rooms lets users check available rooms and make reservations. It includes features for adding and updating room details, searching for available rooms, and booking them for specific dates.

## Table of Contents

- [Installation](#installation)
- [Test Data](#data)
- [Endpoints](#endpoints)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MilyB33/django-hotel-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd django-hotel-api
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Data

There are already some demo data in database:

staff/admin user:

- username: admin
- password: admin

regular user 1:

- username: test1
- email: test1@example.com
- password: test0987654321

regular user 2:

- username: test2
- email: test2@example.com
- password: test0987654321

## Endpoints

#### Authentication

| HTTP Method | Endpoint        | Description                 |
| ----------- | --------------- | --------------------------- |
| POST        | /auth/register/ | Register a new user.        |
| POST        | /auth/login/    | Login and get access token. |
| POST        | /auth/logout/   | Logout the user.            |

#### Hotels

| HTTP Method | Endpoint       | Description                      |
| ----------- | -------------- | -------------------------------- |
| GET         | /hotels/       | List all hotels.                 |
| POST        | /hotels/       | Create a new hotel (admin only). |
| GET         | /hotels/\<id>/ | Retrieve details of a hotel.     |
| PUT/PATCH   | /hotels/\<id>/ | Update a hotel (admin only).     |
| DELETE      | /hotels/\<id>/ | Delete a hotel (admin only).     |

#### Rooms

| HTTP Method | Endpoint                  | Description                     |
| ----------- | ------------------------- | ------------------------------- |
| GET         | /hotels/<hotel_id>/rooms/ | List all rooms in a hotel.      |
| POST        | /hotels/<hotel_id>/rooms/ | Create a new room (admin only). |
| GET         | /rooms/\<id>/             | Retrieve details of a room.     |
| PUT         | /rooms/\<id>/             | Update a room (admin only).     |
| DELETE      | /rooms/\<id>/             | Delete a room (admin only).     |

#### Reservations

| HTTP Method | Endpoint             | Description                            |
| ----------- | -------------------- | -------------------------------------- |
| GET         | /reservations/       | List all reservations (admin only).    |
| POST        | /reservations/       | Create a new reservation.              |
| GET         | /reservations/\<id>/ | Retrieve details of a reservation.     |
| PUT         | /reservations/\<id>/ | Update a reservation.                  |
| DELETE      | /reservations/\<id>/ | Cancel/delete a reservation.           |
| GET         | /users/reservations/ | List reservations for a specific user. |

#### Reviews

| HTTP Method | Endpoint                          | Description                            |
| ----------- | --------------------------------- | -------------------------------------- |
| GET         | /hotels/<reservation_id>/reviews/ | List all reviews for a reservation.    |
| POST        | /hotels/<reservation_id>/reviews/ | Create a new review for a reservation. |
| GET         | /reviews/\<id>/                   | Retrieve details of a review.          |
| PUT         | /reviews/\<id>/                   | Update a review.                       |
| DELETE      | /reviews/\<id>/                   | Delete a review.                       |
| GET         | /hotels/<hotel_id>/reviews/       | List reviews for a specific hotel      |
