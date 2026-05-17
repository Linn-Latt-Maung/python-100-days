class Rocket:
    def __init__(self, name):
        # Initializing the rocket's name and its starting point in 3D Space
        self.name = name
        self.x = 0
        self.y = 0
        self.z = 0  # Z represents Altitude (Up/Down)
        self.fuel = 100
        self.telemetry_log = []

    def move(self, dx, dy, dz):
        # 1. Guard Logic: Stop execution if there is no fuel left
        if self.fuel <= 0:
            print(f"⚠️ {self.name} has no fuel left! Action denied.")
            return False
        
        # 2. Movement Logic: Add the delta changes to current coordinates
        self.x += dx
        self.y += dy
        self.z += dz
        
        # 3. Consumption Logic: Burn 10 units of fuel per maneuver
        self.fuel -= 10
        if self.fuel < 0:
            self.fuel = 0 # Prevent negative fuel percentages
        
        # 4. Logging Logic: Save a snapshot of this position into the recorder
        self.telemetry_log.append({
            "action": "Moved", 
            "position": (self.x, self.y, self.z)
        })
        return True

    def refuel(self):
        # Reset fuel capacity back to max
        self.fuel = 100
        self.telemetry_log.append({
            "action": "Refueled", 
            "position": (self.x, self.y, self.z)
        })
        print(f"⛽ {self.name} has been successfully refueled.")

    def print_log(self):
        # 5. Loop Logic: Iterate and unpack our dictionary records gracefully
        print(f"\n--- Flight Data Recorder: {self.name} ---")
        for index, log in enumerate(self.telemetry_log, start=1):
            action = log["action"]
            pos = log["position"]
            print(f"Step {index}: [{action}] -> Current Vector Position: {pos}")

    def __str__(self):
        # 6. Formatting Logic: Building a clean text dashboard using alignment mechanics
        title = f"{self.name:=^30}\n"
        coordinates = f"Position Vector : X: {self.x}, Y: {self.y}, Z: {self.z}\n"
        fuel_status = f"Fuel Capacity   : {self.fuel}%\n"
        border = "=" * 30
        return title + coordinates + fuel_status + border


# ==========================================
#               TEST BENCH
# ==========================================

# Step 1: Initialize our virtual object instance
apollo = Rocket("Apollo 11")
print("--- Initial State ---")
print(apollo)

# Step 2: Simulate dynamic spatial changes (moving the object)
print("\n--- Executing Flight Plan ---")
apollo.move(10, 5, 80)     # Launch phase: blasting high into the Z-axis
apollo.move(5, -2, 120)    # Orbit adjustment
apollo.move(0, 15, -10)    # Forward cruise
print(apollo)

# Step 3: Run dry out of fuel to test guard defenses
print("\n--- Testing Fuel Depletion Guard ---")
for i in range(8): 
    apollo.move(1, 1, 1)   # Burn the remaining fuel cycles

print(apollo)
apollo.move(5, 5, 5)       # This movement attempt should get blocked safely!

# Step 4: Maintenance operations
print("\n--- Ground Control Command ---")
apollo.refuel()
print(apollo)

# Step 5: Read structural history logs
apollo.print_log()