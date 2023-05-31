# WeatherData

* [API Documentation](./docs/API_Docs.md)
* [Design Doc](https://docs.google.com/document/d/1w0xrrAR_tPXZ2uAZr1cgVVtUw0cLqIgsrHz2ME_ZzG0/edit?usp=sharing)

### Running the application

1. Navigate to the `weatherdata` folder
2. `docker build -t weather-data .`
3. `docker run -p 8000:8000 weather-data`
4. Go to http://127.0.0.1:8000/weather/ to access the app
