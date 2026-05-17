import time

class Rocket:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.z = 0  # Z is Altitude
        self.fuel = 100
        self.telemetry_log = []

    def move(self, dx, dy, dz):
        if self.fuel <= 0:
            print(f"⚠️ {self.name} has no fuel left! Action denied.")
            return False
        
        self.x += dx
        self.y += dy
        self.z += dz
        self.fuel -= 10
        if self.fuel < 0: self.fuel = 0
        
        self.telemetry_log.append({
            "action": "Moved", 
            "position": (self.x, self.y, self.z)
        })
        return True

    def refuel(self):
        self.fuel = 100
        self.telemetry_log.append({
            "action": "Refueled", 
            "position": (self.x, self.y, self.z)
        })
        print(f"⛽ {self.name} has been successfully refueled.")

    # ==========================================
    #        🆕 NEW: LANDING SIMULATION
    # ==========================================
    def landing_simulation(self):
        print(f"\n{" PRE-LANDING SEQUENCE STARTED ":=^50}")
        print(f"Initiating descent protocol for {self.name}...")
        
        # Set a starting high altitude if the rocket is currently on the ground
        if self.z <= 0:
            self.z = 100 
            
        velocity = 0  # Speed of descent
        gravity = 5   # Constant pull downwards
        
        print(f"Starting Altitude: {self.z}m | Current Fuel: {self.fuel}%")
        print("-" * 50)
        
        # The game loop runs while the rocket is still in the air
        while self.z > 0:
            # 1. Apply gravity to velocity, and update altitude
            velocity += gravity
            self.z -= velocity
            
            # If the calculation drops below 0, clip it to 0 (the ground)
            if self.z < 0: 
                self.z = 0
                
            print(f"Altitude: {self.z:>3}m | Descent Speed: {velocity:>2} m/s | Fuel: {self.fuel}%")
            
            # If still in the air, let the player choose to burn fuel
            if self.z > 0:
                if self.fuel >= 10:
                    choice = input("Press [B] to burn thrusters (Slows descent) or Enter to coast: ").strip().lower()
                    if choice == 'b':
                        self.fuel -= 10
                        velocity -= 15 # Counteract gravity with engine thrust
                        print("🔥 Thrusters Fired! Speed reduced.")
                else:
                    print("⚠️ OUT OF FUEL! Free falling...")
                    time.sleep(0.5) # Adds a dramatic delay to the text game
                    
        # 2. Check Win/Loss conditions when hitting the ground (Z = 0)
        print("-" * 50)
        print("🚨 TOUCHDOWN! Analyzing impact telemetry...")
        time.sleep(1)
        
        if velocity <= 10:
            print(f"🎉 SUCCESS! {self.name} has landed smoothly. The crew is safe!")
            self.telemetry_log.append({"action": "Safe Landing", "position": (self.x, self.y, self.z)})
        else:
            print(f"💥 CRASH! {self.name} hit the surface too fast at {velocity} m/s.")
            print("The rocket exploded on impact.")
            self.telemetry_log.append({"action": "Crashed on Landing", "position": (self.x, self.y, self.z)})
            
        print("=" * 50)

    def __str__(self):
        title = f"{self.name:=^30}\n"
        coordinates = f"Position Vector : X: {self.x}, Y: {self.y}, Z: {self.z}\n"
        fuel_status = f"Fuel Capacity   : {self.fuel}%\n"
        border = "=" * 30
        return title + coordinates + fuel_status + border

# ==========================================
#               TEST BENCH
# ==========================================
# Create the rocket
falcon = Rocket("Falcon 9")

# Give it some initial movements to use up a bit of fuel
falcon.move(0, 0, 150) 
falcon.move(0, 0, 200)

# Start the interactive landing mini-game!
falcon.landing_simulation()
