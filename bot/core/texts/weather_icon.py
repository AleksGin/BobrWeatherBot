class TypesWeatherCodes:
    THUNDERSTORM_START = 200
    THUNDERSTORM_END = 232
    DRIZZLE_START = 300
    DRIZZLE_END = 321
    RAIN_START = 500
    FREEZING_RAIN = 511
    RAIN_END = 531
    SNOW_START = 600
    SNOW_END = 622
    ATMOSPHERE_START = 701
    ATMOSPHERE_END = 781
    CLEAR_SKY = 800
    FEW_CLOUDS = 801
    SCRATTED_CLOUDS = 802
    CLOUDS_START = 803
    CLOUDS_END = 804


class WeatherIcon:
    weather_icon = {
        TypesWeatherCodes.CLEAR_SKY: "🌞",
        TypesWeatherCodes.FEW_CLOUDS: "🌤",
        TypesWeatherCodes.SCRATTED_CLOUDS: "⛅",
        **{i: "🌩" for i in range(200, 233)},
        **{i: "🌧" for i in range(300, 322)},
        **{i: "🌧" for i in range(500, 532)},
        **{i: "⛄" for i in range(600, 623)},
        **{i: "🌫" for i in range(701, 782)},
        **{i: "🌫" for i in range(803, 805)},
    }
