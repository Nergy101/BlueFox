from geo_service import GeoService

geo_service = GeoService()
geo_service.add_location("thuis", "Tweede Westerparklaan", "202")
geo_service.save_all_locations()
home = geo_service.get_location("thuis").toString().split(', ')
print(home[1], home[0], home[2], home[4], home[5])
