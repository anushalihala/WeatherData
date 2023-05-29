import unittest
from django.test import Client
import datetime

# Create your tests here.
class TestRegionAll(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.current_year = datetime.date.today().year

    def test_nonexistant_region(self):
        response = self.client.get("/weather/region/U/")
        self.assertEqual(response.status_code, 404)

    def test_year_count(self):
        response = self.client.get("/weather/region/UK/")
        self.assertEqual(len(response.json()), (self.current_year-1836+1)*12) # current year and 1836 inclusive

class TestRegionTimespan(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_empty_timespan1(self):
        response = self.client.get("/weather/region/UK/start/2100/end/2150/")
        self.assertEqual(response.status_code, 404)

    def test_empty_timespan2(self):
        response = self.client.get("/weather/region/UK/start/1980/end/1970/")
        self.assertEqual(response.status_code, 404)

    def test_timespan(self):
        response = self.client.get("/weather/region/UK/start/1990/end/2000/")
        self.assertEqual(len(response.json()), (2000 - 1990 + 1) * 12)

    def test_data_1836(self):
        response = self.client.get("/weather/region/UK/start/1836/end/1836/")
        response = response.json()
        self.assertEqual(response[0]["tmax"], None)
        self.assertEqual(response[0]["rainfall"], 101.5)
        self.assertEqual(response[0]["airfrost"], None)
        self.assertEqual(response[-1]["tmax"], None)
        self.assertEqual(response[-1]["rainfall"], 108.6)
        self.assertEqual(response[-1]["airfrost"], None)

    def test_data_1884(self):
        response = self.client.get("/weather/region/UK/start/1884/end/1884/")
        response = response.json()
        self.assertEqual(response[0]["tmax"], 7.3)
        self.assertEqual(response[0]["rainfall"], 142.9)
        self.assertEqual(response[0]["airfrost"], None)
        self.assertEqual(response[-1]["tmax"], 5.8)
        self.assertEqual(response[-1]["rainfall"], 125.6)
        self.assertEqual(response[-1]["airfrost"], None)

    def test_data_1960(self):
        response = self.client.get("/weather/region/UK/start/1960/end/1960/")
        response = response.json()
        self.assertEqual(response[0]["tmax"], 5.8)
        self.assertEqual(response[0]["rainfall"], 123.4)
        self.assertEqual(response[0]["airfrost"], 15.8)
        self.assertEqual(response[-1]["tmax"], 5.6)
        self.assertEqual(response[-1]["rainfall"], 125.9)
        self.assertEqual(response[-1]["airfrost"], 14.4)

    def test_data_1910(self):
        response = self.client.get("/weather/region/UK/start/1910/end/1910/")
        response = response.json()
        self.assertEqual(response[0]["tmin"], -0.4)
        self.assertEqual(response[0]["sunshine"], 50.9)
        self.assertEqual(response[0]["raindays1mm"], 17.1)
        self.assertEqual(response[-1]["tmin"], 3)
        self.assertEqual(response[-1]["sunshine"], 29.9)
        self.assertEqual(response[-1]["raindays1mm"], 20.2)

    def test_data_2000(self):
        response = self.client.get("/weather/region/UK/start/2000/end/2000/")
        response = response.json()
        self.assertEqual(response[0]["tmean"], 4.3)
        self.assertEqual(response[0]["sunshine"], 57.9)
        self.assertEqual(response[0]["raindays1mm"], 12.0)
        self.assertEqual(response[-1]["tmean"], 4.6)
        self.assertEqual(response[-1]["sunshine"], 40.2)
        self.assertEqual(response[-1]["raindays1mm"], 17.3)

    def test_data_1884_EnglandSEC(self):
        response = self.client.get("/weather/region/England_SE_and_Central_S/start/1884/end/1884/")
        response = response.json()
        self.assertEqual(response[0]["tmean"], 6.1)
        self.assertEqual(response[0]["sunshine"], None)
        self.assertEqual(response[0]["raindays1mm"], None)
        self.assertEqual(response[-1]["tmean"], 4.7)
        self.assertEqual(response[-1]["sunshine"], None)
        self.assertEqual(response[-1]["raindays1mm"], None)

    def test_data_2000_EnglandSEC(self):
        response = self.client.get("/weather/region/England_SE_and_Central_S/start/2000/end/2000/")
        response = response.json()
        self.assertEqual(response[0]["tmean"], 4.6)
        self.assertEqual(response[0]["sunshine"], 72.0)
        self.assertEqual(response[0]["raindays1mm"], 5.5)
        self.assertEqual(response[-1]["tmean"], 6.1)
        self.assertEqual(response[-1]["sunshine"], 41.5)
        self.assertEqual(response[-1]["raindays1mm"], 16.0)

class Test2023(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_tmax(self):
        response = self.client.get("/weather/region/UK/start/2023/end/2023/")
        response = response.json()
        self.assertEqual(response[0]["tmax"], 7.3)
        self.assertEqual(response[1]["tmax"], 9.0)
        self.assertEqual(response[2]["tmax"], 8.9)
        self.assertEqual(response[3]["tmax"], 11.9)
        # needs to be updated later in the year
        self.assertEqual(response[4]["tmax"], None)
        self.assertEqual(response[11]["tmax"], None)

    def test_rainfall(self):
        response = self.client.get("/weather/region/UK/start/2023/end/2023/")
        response = response.json()
        self.assertEqual(response[0]["rainfall"], 125.7)
        self.assertEqual(response[1]["rainfall"], 43.4)
        self.assertEqual(response[2]["rainfall"], 132.0)
        self.assertEqual(response[3]["rainfall"], 69.8)
        # needs to be updated later in the year
        self.assertEqual(response[4]["rainfall"], None)
        self.assertEqual(response[11]["rainfall"], None)