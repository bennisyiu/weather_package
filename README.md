# This app is to get the weather forecast for the next 12 hours of the city or the coordinates of your choiceself.
    Package use example:

    # Usecase I: Create the Weather object using a city name:
    # weather = Weather(apikey={'your own api key'}, city='London')
    # Go get your own api key from https://openweathermap.org/

    # Usecase II: Create the Weather object using coordinates:
    # weather = Weather(apikey={'your own api key'}, lat=22.3, lon=114.1)

    # Get complete data for the next 12 hours:
    # weather.next_12h()

    # Get simplified data for the next 12 hours:
    # weather.next_12h_simplified()
