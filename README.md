# Vehicle Rental System

**Python vehicle-rental system with OOP & LLD included**

A clean, object-oriented demo application for managing a fleet of cars,bikes and trucks, complete with reservation lifecycle, billing, and payment processing. Includes low-level design artifacts (UML class and sequence diagrams).

---


# Features

- **Fleet Inventory Management**  
  - Add, remove, and list vehicles by type (CAR, BIKE, TRUCK)  
- **Reservation Lifecycle**  
  - Schedule (`DAILY`/`HOURLY`), track status (`SCHEDULED`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED`)  
- **Billing & Payments**  
  - Generate bills, process payments (`CASH`/`ONLINE`), mark as paid  
- **Status Safety**  
  - Uses Python `Enum` for strong typing of statuses and types  
- **Low-Level Design**  
  - UML class & sequence diagrams demonstrating key design patterns  


Extensible design: easy to add new vehicle types, billing rules, or a front-end
![UML](UML_CAR_RENTAL.png)
