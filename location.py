class Location:

    def __init__(self, name, street, house_number, lat, lon, display_name):
        self.name = name
        self.house_number = house_number
        self.lat = lat
        self.lon = lon
        self.display_name = display_name

    def toString(self):
        return self.display_name
