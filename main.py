import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books by changing the availability from yes to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotel.csv", index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    def view_hotels(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Reserved.
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_obj=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")
