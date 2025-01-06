# Create class for hotel data.
class Hotel:
    sortParam = 'name'

    def __init__(self) -> None:
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = 0
        self.pricePr = 0

    def __lt__(self, other):
        return getattr(self, Hotel.sortParam) < getattr(other, Hotel.sortParam)

    @classmethod
    def sortByName(cls):
        cls.sortParam = 'name'

    @classmethod
    def sortByRate(cls):
        cls.sortParam = 'rating'

    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam = 'roomAvl'

    def __repr__(self) -> str:
        return f"HotelName: {self.name}, Rooms: {self.roomAvl}, Location: {self.location}, Rating: {self.rating}, PricePerRoom: {self.pricePr}"


# Create class for user data.
class User:
    def __init__(self) -> None:
        self.uname = ''
        self.uId = 0
        self.cost = 0

    def __repr__(self) -> str:
        return f"UserName: {self.uname}, UserId: {self.uId}, BookingCost: {self.cost}"


# Print hotel data.
def print_hotel_data(hotels):
    for hotel in hotels:
        print(hotel)


# Sort hotels by name.
def sort_hotels_by_name(hotels):
    print("SORT BY NAME:")
    Hotel.sortByName()
    hotels.sort()
    print_hotel_data(hotels)
    print()


# Sort hotels by rating.
def sort_hotels_by_rating(hotels):
    print("SORT BY RATING:")
    Hotel.sortByRate()
    hotels.sort(reverse=True)  # Higher rating first
    print_hotel_data(hotels)
    print()


# Print hotels by location.
def print_hotels_by_city(location, hotels):
    print(f"HOTELS IN {location.upper()}:")
    hotels_by_location = [hotel for hotel in hotels if hotel.location == location]
    print_hotel_data(hotels_by_location)
    print()


# Sort hotels by room availability.
def sort_hotels_by_room_availability(hotels):
    print("SORT BY ROOM AVAILABILITY:")
    Hotel.sortByRoomAvailable()
    hotels.sort(reverse=True)  # More rooms first
    print_hotel_data(hotels)
    print()


# Print user data and associated hotels.
def print_user_data(user_names, user_ids, booking_costs, hotels):
    users = []
    for i in range(len(user_names)):
        user = User()
        user.uname = user_names[i]
        user.uId = user_ids[i]
        user.cost = booking_costs[i]
        users.append(user)

    for i in range(len(users)):
        print(f"{users[i]} - Hotel: {hotels[i].name}")


# Function to manage hotel data.
def hotel_management(user_names, user_ids, hotel_names, booking_costs, rooms, locations, ratings, prices):
    hotels = []

    # Initialize hotel data.
    for i in range(len(hotel_names)):
        hotel = Hotel()
        hotel.name = hotel_names[i]
        hotel.roomAvl = rooms[i]
        hotel.location = locations[i]
        hotel.rating = ratings[i]
        hotel.pricePr = prices[i]
        hotels.append(hotel)

    print("\nHOTEL DATA:")
    print_hotel_data(hotels)
    print()

    # Perform sorting and filtering operations.
    sort_hotels_by_name(hotels)
    sort_hotels_by_rating(hotels)
    print_hotels_by_city("Bangalore", hotels)
    sort_hotels_by_room_availability(hotels)
    print_user_data(user_names, user_ids, booking_costs, hotels)


# Driver code.
if __name__ == '__main__':
    user_names = ["U1", "U2", "U3"]
    user_ids = [2, 3, 4]
    hotel_names = ["H1", "H2", "H3"]
    booking_costs = [1000, 1200, 1100]
    rooms = [4, 5, 6]
    locations = ["Bangalore", "Bangalore", "Mumbai"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100]

    hotel_management(user_names, user_ids, hotel_names, booking_costs, rooms, locations, ratings, prices)
