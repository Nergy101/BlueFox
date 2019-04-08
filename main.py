from geo_service import GeoService
from tqdm import tqdm

geo_service = GeoService()
geo_service.add_location("thuis", "Tweede Westerparklaan", "202")
geo_service.add_location("vriendin", "Monarchvlinderlaan", "19")

geo_service.save_all_locations()

for l in tqdm(geo_service.get_all_locations()):
    print(l.display_name)
