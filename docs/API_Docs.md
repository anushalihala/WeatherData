# API Documentation

## Available endpoints

1. GET ```/weather/region/{region}/```<br>
Get weather data for specified region for all available years
2. GET ```/weather/region/{region}/start/{start}/end/{end}/```<br>
Get weather data for specified region for specified time range.

## Parameters

| parameter | type | description |
------------|------|---------------
region | string | Region of the weather data. One of "UK", "England", "Wales", "Scotland", "Northern_Ireland", "England_and_Wales", "England_N", "England_S", "Scotland_N", "Scotland_E", "Scotland_W", "England_E_and_NE", "England_NW_and_N_Wales", "Midlands", "East_Anglia", "England_SW_and_S_Wales", or "England_SE_and_Central_S".
start | number | Year from which weather data will be available (inclusive).
end | number | Year till which weather data will be available (inclusive).

## Response Schema

| property | type | nullable? | description
-----------|------|-----------|-------------
region | string | No | The region for which weather data is provided
month | string | No | 3 character month name
year | integer | No | Year in which associated metrics were recorded
tmax | float | Yes | Monthly mean of daily maximum air temperature
tmin | float | Yes | Monthly mean of daily minimum air temperature
tmean | float | Yes | Monthly mean air temperature
sunshine | float | Yes | Monthly total duration of bright sunshine
rainfall | float | Yes | Monthly total precipitation amount
raindays1mm | float | Yes | Monthly number of days in the month with precipitation amount >= 1mm
airfrost | float | Yes | Monthly number of days in the month with air frost (minimum temperature below zero)

## Examples
Request <br>
```/weather/region/UK/```

Sample truncated response <br>
```
[
  {
    "region": "UK",
    "month": "jan",
    "year": 1836,
    "tmax": null,
    "tmin": null,
    "tmean": null,
    "sunshine": null,
    "rainfall": 101.5,
    "raindays1mm": null,
    "airfrost": null
  },
  ...
  {
    "region": "UK",
    "month": "dec",
    "year": 2023,
    "tmax": null,
    "tmin": null,
    "tmean": null,
    "sunshine": null,
    "rainfall": null,
    "raindays1mm": null,
    "airfrost": null
  }
]
  ```
Request <br>
```/weather/region/England/start/2000/end/2001```

Sample response <br>
```
[
  {
    "region": "England",
    "month": "jan",
    "year": 2000,
    "tmax": 7.6,
    "tmin": 1.5,
    "tmean": 4.6,
    "sunshine": 69.4,
    "rainfall": 46.4,
    "raindays1mm": 7.9,
    "airfrost": 10.0
  },
  {
    "region": "England",
    "month": "feb",
    "year": 2000,
    "tmax": 9.1,
    "tmin": 2.6,
    "tmean": 5.8,
    "sunshine": 95.7,
    "rainfall": 85.1,
    "raindays1mm": 16.0,
    "airfrost": 5.4
  },
  {
    "region": "England",
    "month": "mar",
    "year": 2000,
    "tmax": 10.8,
    "tmin": 3.4,
    "tmean": 7.1,
    "sunshine": 118.8,
    "rainfall": 34.0,
    "raindays1mm": 6.6,
    "airfrost": 4.8
  },
  {
    "region": "England",
    "month": "apr",
    "year": 2000,
    "tmax": 11.5,
    "tmin": 3.7,
    "tmean": 7.6,
    "sunshine": 137.7,
    "rainfall": 131.9,
    "raindays1mm": 18.3,
    "airfrost": 4.2
  },
  {
    "region": "England",
    "month": "may",
    "year": 2000,
    "tmax": 16.2,
    "tmin": 7.2,
    "tmean": 11.7,
    "sunshine": 193.2,
    "rainfall": 83.1,
    "raindays1mm": 12.9,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "jun",
    "year": 2000,
    "tmax": 18.8,
    "tmin": 10.2,
    "tmean": 14.5,
    "sunshine": 165.3,
    "rainfall": 42.4,
    "raindays1mm": 7.8,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "jul",
    "year": 2000,
    "tmax": 19.1,
    "tmin": 10.7,
    "tmean": 14.9,
    "sunshine": 154.5,
    "rainfall": 60.3,
    "raindays1mm": 10.0,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "aug",
    "year": 2000,
    "tmax": 21.1,
    "tmin": 11.6,
    "tmean": 16.3,
    "sunshine": 194.0,
    "rainfall": 61.4,
    "raindays1mm": 11.0,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "sep",
    "year": 2000,
    "tmax": 18.4,
    "tmin": 10.6,
    "tmean": 14.5,
    "sunshine": 115.9,
    "rainfall": 116.8,
    "raindays1mm": 14.1,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "oct",
    "year": 2000,
    "tmax": 13.4,
    "tmin": 6.7,
    "tmean": 10.0,
    "sunshine": 91.9,
    "rainfall": 166.8,
    "raindays1mm": 18.4,
    "airfrost": 0.2
  },
  {
    "region": "England",
    "month": "nov",
    "year": 2000,
    "tmax": 9.6,
    "tmin": 3.6,
    "tmean": 6.6,
    "sunshine": 60.5,
    "rainfall": 160.1,
    "raindays1mm": 19.1,
    "airfrost": 1.6
  },
  {
    "region": "England",
    "month": "dec",
    "year": 2000,
    "tmax": 7.7,
    "tmin": 3.0,
    "tmean": 5.3,
    "sunshine": 47.3,
    "rainfall": 120.7,
    "raindays1mm": 16.0,
    "airfrost": 8.5
  },
  {
    "region": "England",
    "month": "jan",
    "year": 2001,
    "tmax": 5.9,
    "tmin": 0.4,
    "tmean": 3.1,
    "sunshine": 75.0,
    "rainfall": 69.9,
    "raindays1mm": 11.0,
    "airfrost": 14.4
  },
  {
    "region": "England",
    "month": "feb",
    "year": 2001,
    "tmax": 7.7,
    "tmin": 0.7,
    "tmean": 4.2,
    "sunshine": 86.8,
    "rainfall": 90.7,
    "raindays1mm": 12.8,
    "airfrost": 14.0
  },
  {
    "region": "England",
    "month": "mar",
    "year": 2001,
    "tmax": 8.2,
    "tmin": 1.7,
    "tmean": 4.9,
    "sunshine": 89.1,
    "rainfall": 87.5,
    "raindays1mm": 14.4,
    "airfrost": 9.3
  },
  {
    "region": "England",
    "month": "apr",
    "year": 2001,
    "tmax": 11.2,
    "tmin": 3.5,
    "tmean": 7.4,
    "sunshine": 133.1,
    "rainfall": 91.4,
    "raindays1mm": 16.4,
    "airfrost": 2.8
  },
  {
    "region": "England",
    "month": "may",
    "year": 2001,
    "tmax": 17.0,
    "tmin": 7.0,
    "tmean": 12.0,
    "sunshine": 229.7,
    "rainfall": 39.8,
    "raindays1mm": 6.3,
    "airfrost": 0.3
  },
  {
    "region": "England",
    "month": "jun",
    "year": 2001,
    "tmax": 18.4,
    "tmin": 9.1,
    "tmean": 13.7,
    "sunshine": 193.9,
    "rainfall": 41.0,
    "raindays1mm": 6.7,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "jul",
    "year": 2001,
    "tmax": 21.3,
    "tmin": 12.0,
    "tmean": 16.7,
    "sunshine": 193.4,
    "rainfall": 68.0,
    "raindays1mm": 9.6,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "aug",
    "year": 2001,
    "tmax": 21.0,
    "tmin": 12.0,
    "tmean": 16.5,
    "sunshine": 180.2,
    "rainfall": 78.8,
    "raindays1mm": 13.1,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "sep",
    "year": 2001,
    "tmax": 16.7,
    "tmin": 9.4,
    "tmean": 13.1,
    "sunshine": 114.2,
    "rainfall": 78.8,
    "raindays1mm": 13.4,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "oct",
    "year": 2001,
    "tmax": 16.2,
    "tmin": 10.0,
    "tmean": 13.1,
    "sunshine": 104.6,
    "rainfall": 119.5,
    "raindays1mm": 16.3,
    "airfrost": 0.0
  },
  {
    "region": "England",
    "month": "nov",
    "year": 2001,
    "tmax": 10.6,
    "tmin": 3.6,
    "tmean": 7.1,
    "sunshine": 69.2,
    "rainfall": 57.7,
    "raindays1mm": 10.8,
    "airfrost": 5.0
  },
  {
    "region": "England",
    "month": "dec",
    "year": 2001,
    "tmax": 6.6,
    "tmin": 0.2,
    "tmean": 3.3,
    "sunshine": 75.4,
    "rainfall": 39.4,
    "raindays1mm": 8.5,
    "airfrost": 17.6
  }
]
```