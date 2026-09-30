class VacuumCleaner:
    def __init__(self):
        self.battery = 100
        self.cleaned_rooms = ["Living Room"]
        self.memory = []

    def clean_room(self, room, battery_required):
        print(f"\nTrying to clean: {room}")
        print(f"Battery available: {self.battery}%")
        print(f"Battery required: {battery_required}%")

        if room in self.cleaned_rooms:
            print(f"{room} was already cleaned. Skipping.")
            return

        if self.battery >= battery_required:
            self.battery -= battery_required
            self.cleaned_rooms.append(room)

            self.memory.append({
                "room": room,
                "battery_used": battery_required,
                "battery_remaining": self.battery
            })

            print(f"✓ {room} cleaned successfully.")
            print(f"Battery remaining: {self.battery}%")

        else:
            print(f"✗ Not enough battery to clean {room}.")
            print(f"Need {battery_required}%, but only {self.battery}% is available.")

    def show_memory(self):
        print("\n--- Vacuum Memory ---")

        for record in self.memory:
            print(
                f"Room: {record['room']} | "
                f"Battery used: {record['battery_used']}% | "
                f"Remaining: {record['battery_remaining']}%"
            )

        print(f"\nCurrent battery: {self.battery}%")
        print(f"Cleaned rooms: {self.cleaned_rooms}")


vacuum = VacuumCleaner()

print("Vacuum started with 100% battery.")

rooms = [
    ("Living Room", 20),
    ("Kitchen", 25),
    ("Bedroom", 15),
    ("Bathroom", 20),
    ("Study Room", 15)
]

for room, battery_required in rooms:
    vacuum.clean_room(room, battery_required)

vacuum.show_memory()