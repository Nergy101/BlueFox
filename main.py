from geo_service import GeoService
from tqdm import tqdm

geo_service = GeoService()
geo_service.add_location("thuis", "Tweede Westerparklaan", "202")
geo_service.add_location("vriendin", "Mondriaanerf", "19")
geo_service.add_location("werk", "Atoomweg", "63")

geo_service.save_all_locations()

print('Locations')
for l in geo_service.get_all_locations():
    print("- "+l.name+": "+l.display_name)
