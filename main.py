import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "holder": holder,
                     "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False




print(df)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard("1234")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        passw = input("Enter the password: ")
        if credit_card.authenticate(given_password=passw):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_obj=hotel)
            print(reservation_ticket.generate())
        else:
            print("Wrong Passw")
    else:
        print("Billing problem")
else:
    print("Hotel is not free")
