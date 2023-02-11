

class Place:
    def __init__(self, place_dict):
        self._id = place_dict.get('_id')
        self.google_place_business_status = place_dict.get('business_status')
        self.geometry = place_dict.get('geometry')
        self.google_place_icon = place_dict.get('icon')
        self.icon_background_color = place_dict.get('icon_background_color')
        self.icon_mask_base_uri = place_dict.get('icon_mask_base_uri')
        self.google_place_name = place_dict.get('name')
        # self.opening_hours = place_dict.get('opening_hours')
        self.google_place_photos = place_dict.get('photos')
        self.google_place_id = place_dict.get('place_id')
        # self.plus_code = place_dict.get('plus_code')
        self.google_place_rating = place_dict.get('rating')
        # self.reference = place_dict.get('reference')
        self.google_place_scope = place_dict.get('scope')
        self.google_place_types = place_dict.get('types')
        self.google_place_user_ratings_total = place_dict.get('user_ratings_total')
        self.google_place_address = place_dict.get('vicinity')
        self.google_place_csz = place_dict.get('csz')
        self.google_place_category = place_dict.get('category')