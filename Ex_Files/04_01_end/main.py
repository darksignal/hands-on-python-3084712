import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    #DRG To avoid an error, we need to check if the value is None (I get an error on the year 2023)
    if year["value"] is None:
        year["value"] = 0
    display_width = year["value"] // 10_000_000
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)
