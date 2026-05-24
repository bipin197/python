from dataApi.cricketApi import get_all_cricket_series_data, get_cricket_series_data

def main():
    apiKey = ""
    cricket_all_series_data = get_all_cricket_series_data(apiKey)
    dataTable = cricket_all_series_data.get("data", [])
    for series in dataTable:
        print(f"Series ID: {series.get('id')}, Series Name: {series.get('name')}")  
    series_id = input()
    cricket_series_data = get_cricket_series_data(series_id, apiKey)      
    print(cricket_series_data)

if __name__ == "__main__":
    main()