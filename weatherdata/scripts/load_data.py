import urllib.request
from ukmetoffice.models import Month, Region, Weather

# initialise constants
regions = [
    "UK",
   "England",
   "Wales",
   "Scotland",
   "Northern_Ireland",
   "England_and_Wales",
   "England_N",
   "England_S",
   "Scotland_N",
   "Scotland_E",
   "Scotland_W",
   "England_E_and_NE",
   "England_NW_and_N_Wales",
   "Midlands",
   "East_Anglia",
   "England_SW_and_S_Wales",
   "England_SE_and_Central_S"
]

metrics = [
    "Tmax",
    "Tmin",
    "Tmean",
    "Sunshine",
    "Rainfall",
    "Raindays1mm",
    "AirFrost"
]

def run():
    # delete old data
    Region.objects.all().delete()
    Month.objects.all().delete()
    Weather.objects.all().delete()


    for region in regions:
        data = {}
        for metric in metrics:
            # get data from metoffice website
            url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{metric}/date/{region}.txt"
            response = urllib.request.urlopen(url)
            text = response.read()
            # parse data into dict
            text = text.split(b"\n")
            for i in range(6, len(text) - 1):  # 6 for headers; -1 for whitespace footer
                row = text[i]
                for j in range(5, 5+7*12, 7):  # Year ends at 5; Each column has a width of 7
                    value = row[j:j+7].strip()
                    if len(value) == 0:
                        value = None
                    else:
                        value = float(value)

                    year = row[0:5].strip().decode("utf-8")
                    month = text[5][j:j+7].strip().decode("utf-8")
                    if year not in data:
                        data[year] = {}
                    if month not in data[year]:
                        data[year][month] = {}
                    data[year][month][metric] = value

        # unpack dict and save to database
        for year, months in data.items():
            for month, metric_values in months.items():
                r, r_created = Region.objects.get_or_create(name=region)
                m, m_created = Month.objects.get_or_create(name=month)
                w = Weather(
                    region=r,
                    month=m,
                    year=int(year),
                    tmax=metric_values.get("Tmax", None),
                    tmin=metric_values.get("Tmin", None),
                    tmean=metric_values.get("Tmean", None),
                    sunshine=metric_values.get("Sunshine", None),
                    rainfall=metric_values.get("Rainfall", None),
                    raindays1mm=metric_values.get("Raindays1mm", None),
                    airfrost=metric_values.get("AirFrost", None)
                )
                w.save()

                print(region, year, month)