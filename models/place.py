#!/usr/bin/python3
"""Module that defines class Place"""


from base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization method for Place."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """String representation of the Place object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
