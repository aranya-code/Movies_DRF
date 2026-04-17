# 🎬 Movie Rating API (Django REST Framework)

A RESTful API built using **Django** and **Django REST Framework** that allows users to manage movies and post ratings/reviews.
This project demonstrates CRUD operations, relational data handling, validation, and API testing.

---

## 🚀 Features

* 📌 Create a movie
* 📌 Get all movies with ratings
* 📌 Get movie details by ID
* 📌 Update movie (budget)
* 📌 Delete movie
* ⭐ Add rating/review for a movie
* ❌ Prevent duplicate movie entries
* ❌ Prevent duplicate reviews by same user on same movie
* 📊 Ratings sorted in ascending order

---
# Movie Dashboard

**[🚀 View the Live Demo Here](https://aranya.pythonanywhere.com)**

---
## 🛠️ Tech Stack

* Python 3.x
* Django
* Django REST Framework
* SQLite (default DB)

---

## 📂 Project Structure

```
Movies_DRF/
│
├── movies/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tests.py
│
├── Movies_DRF/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd Movies_DRF
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run server

```
python manage.py runserver
```

👉 API will be available at:

```
http://127.0.0.1:8000/
```

---

## 📌 API Endpoints

### 🎬 Movie APIs

#### ➤ Create / List Movies

```
GET    /movie/add/
POST   /movie/add/
```

#### ➤ Movie Detail / Update / Delete

```
GET     /movie/movie_detail/<id>/
PUT     /movie/movie_detail/<id>/
DELETE  /movie/movie_detail/<id>/
```

---

### ⭐ Rating API

#### ➤ Add Rating

```
POST /movie/rating_add/
```

---

## 📥 Sample Requests

### ➤ Create Movie

```json
{
  "movie_name": "Titanic",
  "director": "James Cameron",
  "released_year": 1997,
  "story": "Romantic drama",
  "budget": "20000.0000",
  "language": "Eng"
}
```

---

### ➤ Add Rating

```json
{
  "reviewer": "Aranya",
  "review": "Amazing movie",
  "rating": 9.2,
  "movie": 1
}
```

---

## ⚠️ Validations

* Movie name must be unique
* A reviewer can review a movie only once
* Invalid inputs return `400 Bad Request`

---

## 🧪 Running Tests

```
python manage.py test
```

### ✔ Covered Scenarios

* Create movie
* Duplicate movie validation
* Get all movies
* Empty database case
* Get movie by ID
* Invalid ID handling
* Update movie
* Delete movie
* Add rating
* Duplicate rating validation

---

## 📊 Example Response

```json
{
  "movie_name": "Titanic",
  "director": "James Cameron",
  "released_year": 1997,
  "story": "Romantic drama",
  "language": "Eng",
  "budget": "20000.0000",
  "ratings": [
    {
      "reviewer": "Aranya",
      "rating": 9.2
    }
  ]
}
```

---

## 🎯 Key Learnings

* REST API design using Django REST Framework
* Serializer validation and custom validation logic
* One-to-many relationships (Movie → Ratings)
* Handling edge cases and error responses
* Writing API test cases using `APITestCase`

---

## 📌 Future Improvements

* Authentication (JWT / Token-based)
* Pagination & filtering
* Average rating calculation
* Swagger / API documentation
* Deployment (Docker / AWS)

---

## 👨‍💻 Author

**Aranya Majumdar**

---


