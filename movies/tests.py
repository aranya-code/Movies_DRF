from rest_framework.test import APITestCase
from rest_framework import status
from movies.models import Movies, Rating


# -------------------------------
# 🎬 Movie API Tests
# -------------------------------
class MovieAPITest(APITestCase):

    def test_create_movie(self):
        data = {
            "movie_name": "Titanic",
            "director": "James Cameron",
            "released_year": 1997,
            "story": "Romantic drama",
            "budget": "20000.0000",
            "language": "Eng"
        }

        response = self.client.post("/movie/add/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_movie(self):
        Movies.objects.create(
            movie_name="Titanic",
            director="James Cameron",
            released_year=1997,
            story="Drama",
            budget=20000,
            language="Eng"
        )

        data = {
            "movie_name": "Titanic",
            "director": "James Cameron",
            "released_year": 1997,
            "story": "Drama",
            "budget": "20000.0000",
            "language": "Eng"
        }

        response = self.client.post("/movie/add/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_movies(self):
        Movies.objects.create(
            movie_name="Test",
            director="Dir",
            released_year=2000,
            story="Story",
            budget=1000,
            language="Eng"
        )

        response = self.client.get("/movie/add/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_empty_movies(self):
        response = self.client.get("/movie/add/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# -------------------------------
# 🎯 Movie Detail Tests
# -------------------------------
class MovieDetailTest(APITestCase):

    def setUp(self):
        self.movie = Movies.objects.create(
            movie_name="Titanic",
            director="James Cameron",
            released_year=1997,
            story="Drama",
            budget=20000,
            language="Eng"
        )

    def test_get_movie_detail(self):
        response = self.client.get(f"/movie/movie_detail/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_movie_detail(self):
        response = self.client.get("/movie/movie_detail/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_movie(self):
        data = {"budget": "50000.0000"}

        response = self.client.put(
            f"/movie/movie_detail/{self.movie.id}/",
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_movie(self):
        response = self.client.delete(f"/movie/movie_detail/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# -------------------------------
# ⭐ Rating API Tests
# -------------------------------
class RatingAPITest(APITestCase):

    def setUp(self):
        self.movie = Movies.objects.create(
            movie_name="Titanic",
            director="James Cameron",
            released_year=1997,
            story="Drama",
            budget=20000,
            language="Eng"
        )

    def test_add_rating(self):
        data = {
            "reviewer": "Aranya",
            "review": "Amazing movie",
            "rating": 9.0,
            "movie": self.movie.id
        }

        response = self.client.post("/movie/rating_add/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_rating(self):
        Rating.objects.create(
            reviewer="Aranya",
            review="Good",
            rating=8,
            movie=self.movie
        )

        data = {
            "reviewer": "Aranya",
            "review": "Again",
            "rating": 9,
            "movie": self.movie.id
        }

        response = self.client.post("/movie/rating_add/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)