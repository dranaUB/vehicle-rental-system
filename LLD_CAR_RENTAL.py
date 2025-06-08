from abc import ABC, abstractmethod
from enum import Enum

resevation_unique_id=0
class Status(Enum):
        ACTIVE='ACTIVE'
        INACTIVE='INACTIVE'


class VehicleType(Enum):
        CAR='CAR'
        BIKE='BIKE'
        TRUCK='TRUCK'

class ReservationStatus(Enum):
        SCHEDULED='SCHEDULED'
        IN_PROGRESS='IN_PROGRESS'
        COMPLETED='COMPLETED'
        CANCELLED='CANCELLED'

class ReservationType(Enum):
        HOURLY='HOURLY'
        DAILY='DAILY'


class PaymentMode(Enum):
        CASH='CASH'
        ONLINE= 'ONLINE'
class Vehicle(ABC):
    def __init__(
        self,
        vehicle_id,
        vehicle_number,
        vehicle_type,
        company_name,
        model_name,
        km_driven,
        manufacturing_date,
        average,
        cc,
        daily_rental_cost,
        hourly_rental_cost,
        no_of_seats,
        status,
    ):
        self.vehicle_id = vehicle_id
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.company_name = company_name
        self.model_name = model_name
        self.km_driven = km_driven
        self.manufacturing_date = manufacturing_date
        self.average = average
        self.cc = cc
        self.daily_rental_cost = daily_rental_cost
        self.hourly_rental_cost = hourly_rental_cost
        self.no_of_seats = no_of_seats
        self.status = status


class Car(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Bike(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

class Bill:
       def __init__(self,reservation):
             self.reservation=reservation
             self.total_bill_amount=self.compute_bill_amount()
             self.is_bill_paid=False

       def compute_bill_amount(self):
              
              return 150

class PaymentDetails:
       def __init__(self,payment_id,amount_paid,date_of_payment,is_refundable,payment_mode):
               self.payment_id=payment_id
               self.amount_paid=amount_paid
               self.date_of_payment=date_of_payment
               self.is_refundable=is_refundable
               self.payment_mode=payment_mode

class Payment:
       def pay_bill(self,bill,paymentdetails):
              bill.is_bill_paid=True

class Location:
        def __init__(self,    
                    address,
                    pincode,
                    city,
                    state,
                    country
        ):
                  self.address=address
                  self.pincode=pincode
                  self.city=city
                  self.state=state
                  self.country=country

class Reservation:
        def __init__(self):
            self.reservation_id= 0
            self.user=None
            self.vehicle=None
            self.booking_date=None
            self.date_booked_from=None
            self.date_booked_to=None
            self.pick_up_location=None
            self.drop_location=None
            self.reservation_type=None
            self.reservation_status=None
        
        def create_reservation(self,user,vehicle):
             global resevation_unique_id
             self.reservation_id=resevation_unique_id
             self.user=user
             self.vehicle=vehicle
             self.reservation_type=ReservationType.DAILY
             self.reservation_status=ReservationStatus.SCHEDULED

             resevation_unique_id+=1
             return self.reservation_id
        
        def complete(self):
               self.reservation_status=ReservationStatus.COMPLETED

class VehicleInventoryManagement:
        def __init__(self,vehicles):
              self.vehicles=vehicles
        
        def get_vehicle_by_type(self,vehicle_type):
              return [vehicle for vehicle in self.vehicles  if vehicle.vehicle_type == vehicle_type]
        
        def add_vehicle(self,vehicle):
               self.vehicles.append(vehicle)

        def remove_vehicle(self,vehicle_id):
               self.vehicles=[vehicle for vehicle in self.vehicles if vehicle.vehicle_id!=vehicle_id]
              
class Store:
      def __init__(self,store_id,location,vehicles):
           self.store_id=store_id
           self.location=location
           self.inventory=VehicleInventoryManagement(vehicles)
           self.reservations=[]
      
      def get_vehicles(self,vehicle_type):
            return self.inventory.get_vehicle_by_type(vehicle_type)
      
      def create_reservation(self,user,vehicle):
            reservation=Reservation()
            reservation.create_reservation(user,vehicle)
            self.reservations.append(reservation)
            return reservation
      
      def complete_reservation(self,reservation_id):
           for res in self.reservations:
                    if res.reservation_id==reservation_id:
                           res.complete()
                           return True
           return False
           

class User:
    def __init__(self, user_id, user_name, driving_license):
        self.user_id=user_id
        self.user_name=user_name
        self.driving_license=driving_license


class VehicleRentalSystem:
       def __init__(self,stores,users):
            self.stores=stores
            self.users=users

       def get_store(self,city):
            for store in self.stores:
                  if store.location.city==city:
                        return store
            return self.stores[0]

# Testing my code, for generated test cases from gpt
def main():
    # 1. Create some users
    users=[]
    user1 = User(user_id=1, user_name="Alice", driving_license="DL12345")
    users.append(user1)

    # 2. Create some vehicles
    vehicles=[]
    car1 = Car(
        vehicle_id=1,
        vehicle_number="CAR-001",
        vehicle_type=VehicleType.CAR,
        company_name="Toyota",
        model_name="Corolla",
        km_driven=12000.0,
        manufacturing_date="2022-01-15",
        average=15.0,
        cc=1500,
        daily_rental_cost=50.0,
        hourly_rental_cost=10.0,
        no_of_seats=5,
        status=Status.ACTIVE,
    )
    vehicles.append(car1)

    bike1 = Bike(
        vehicle_id=2,
        vehicle_number="BIKE-001",
        vehicle_type=VehicleType.BIKE,
        company_name="Honda",
        model_name="CBR",
        km_driven=8000.0,
        manufacturing_date="2021-08-10",
        average=45.0,
        cc=250,
        daily_rental_cost=25.0,
        hourly_rental_cost=5.0,
        no_of_seats=2,
        status=Status.ACTIVE,
    )
    vehicles.append(bike1)

    # 3. Create a store (with a location)
    store_location = Location(
        address="123 Main St", pincode="560001", city="Bangalore", state="Karnataka", country="India"
    )
    store1 = Store(store_id=1, location=store_location, vehicles=vehicles)

    # 4. Initialize the rental system
    rental_system = VehicleRentalSystem(stores=[store1], users=users)

    # --- Simulated user flow ---
    # 5. User chooses a city (e.g. “Bangalore”) and searches for a store
    chosen_city = "Bangalore"
    store = rental_system.get_store(chosen_city)

    # 6. User fetches all available cars at that store
    available_cars = store.get_vehicles(VehicleType.CAR)
    if not available_cars:
        print("No cars available.")
        return

    # 7. User selects the first car and creates a reservation
    selected_car = available_cars[0]
    reservation = store.create_reservation(user=users[0], vehicle=selected_car)
    print(f"Created reservation ID = {reservation.reservation_id}")

    # 8. Generate a bill and make payment
    bill = Bill(reservation)
    payment_details = PaymentDetails(payment_id=1, amount_paid=bill.total_bill_amount,date_of_payment='21062025',is_refundable='False', payment_mode=PaymentMode.ONLINE)
    payment = Payment()
    payment.pay_bill(bill, payment_details)
    print(f"Bill of ${bill.total_bill_amount} is_paid = {bill.is_bill_paid}")

    # 9. After the trip, complete the reservation
    success = store.complete_reservation(reservation.reservation_id)
    print(f"Reservation {reservation.reservation_id} completed: {success}")


if __name__ == '__main__':
    main()