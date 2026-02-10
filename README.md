# my-first-project
# this is my project. Application named as" safar".
import time
import heapq
import random

class SafarApp:
    def __init__(self):
        # 1. Graph Data (Abbreviated for brevity, can be expanded to 30+)
        self.cities_graph = {
            'Karachi': {'Hyderabad': 160, 'Thatta': 100},
            'Hyderabad': {'Karachi': 160, 'Sukkur': 330, 'Mirpur Khas': 75},
            'Thatta': {'Karachi': 100, 'Badin': 100},
            'Badin': {'Thatta': 100, 'Hyderabad': 110},
            'Sukkur': {'Hyderabad': 330, 'Multan': 440, 'Larkana': 95, 'Quetta': 390},
            'Larkana': {'Sukkur': 95, 'Dadu': 130},
            'Dadu': {'Larkana': 130, 'Hyderabad': 180},
            'Quetta': {'Sukkur': 390, 'Ziarat': 120, 'Sibi': 160},
            'Multan': {'Sukkur': 440, 'Bahawalpur': 95, 'Sahiwal': 170},
            'Lahore': {'Sahiwal': 180, 'Gujranwala': 95, 'Faisalabad': 180},
            'Islamabad': {'Rawalpindi': 15, 'Abbottabad': 120},
            'Rawalpindi': {'Jhelum': 120, 'Islamabad': 15, 'Peshawar': 170},
        }
        
        # 2. Driver Database
        self.riders = [
            {"name": "Ahmed Ali", "phone": "0321-4567890", "plate": "LEC-4567"},
            {"name": "Zubair Khan", "phone": "0300-9876543", "plate": "RI-229"},
            {"name": "M. Usman", "phone": "0333-1122334", "plate": "KHI-8801"},
            {"name": "Faisal Shah", "phone": "0312-5566778", "plate": "MN-442"}
        ]
        
        self.ride_history = []
        self.vehicles = {"Bike": 15, "Mini Car": 35, "AC Car": 60}

    def dijkstra(self, start, end):
        distances = {city: float('inf') for city in self.cities_graph}
        distances[start] = 0
        pq = [(0, start)]
        previous = {city: None for city in self.cities_graph}

        while pq:
            curr_dist, curr_city = heapq.heappop(pq)
            if curr_city == end:
                path = []
                while curr_city:
                    path.insert(0, curr_city)
                    curr_city = previous[curr_city]
                return path, distances[end]
            
            for neighbor, weight in self.cities_graph.get(curr_city, {}).items():
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = curr_city
                    heapq.heappush(pq, (distance, neighbor))
        return None, float('inf')

    def run(self):
        while True:
            print("\n" + "="*30 + "\n   SAFAR RIDE-HAILING\n" + "="*30)
            print("1. Book a Ride\n2. View History\n3. Emergency\n4. Exit")
            choice = input("Select Option: ")

            if choice == '1':
                self.handle_booking()
            elif choice == '2':
                self.show_history()
            elif choice == '3':
                print("\n🚨 SOS: Call 15 or 0800-SAFAR")
            elif choice == '4':
                break

    def handle_booking(self):
        print("\nAvailable Cities:", ", ".join(sorted(self.cities_graph.keys())))
        start = input("Pickup City: ").title()
        end = input("Destination: ").title()

        if start not in self.cities_graph or end not in self.cities_graph:
            print("❌ Invalid City."); return

        path, dist = self.dijkstra(start, end)
        if not path:
            print("❌ No route found."); return

        print(f"\n📍 Route: {' -> '.join(path)}\n📏 Distance: {dist} km")
        
        # Vehicle & Fare
        vehicle = input("Choose (Bike/Mini Car/AC Car): ").title()
        if vehicle not in self.vehicles: return
        fare = dist * self.vehicles[vehicle]
        
        promo = input("Promo Code (Press Enter to skip): ").upper()
        if promo == "WELCOME":
            fare *= 0.8
            print("🔥 20% Discount Applied!")

        print(f"💰 Total Fare: Rs. {fare:.0f}")
        
        # Payment
        print("\nPayment Method: 1. Cash | 2. JazzCash | 3. Card")
        pay_choice = input("Select (1-3): ")
        payment = "Cash" if pay_choice == '1' else "JazzCash" if pay_choice == '2' else "Card"

        # Simulation
        print("\n" + "-"*30)
        self.simulate_ride(start, end, vehicle, fare, payment)

    def simulate_ride(self, start, end, vehicle, fare, payment):
        rider = random.choice(self.riders)
        statuses = ["Searching...", "Rider Assigned!", "On the Way", "Trip Started", "Arrived!"]
        
        for i, s in enumerate(statuses):
            print(f"🔄 Status: {s}")
            if i == 1:
                print(f"   👤 Rider: {rider['name']} | 📞 {rider['phone']} | 🚗 {rider['plate']}")
            time.sleep(1.5)

        # Rating
        rating = input("\nRate your experience (1-5 stars): ")
        
        # Save History
        self.ride_history.append({
            "date": time.ctime(),
            "route": f"{start} to {end}",
            "fare": fare,
            "vehicle": vehicle,
            "rider": rider['name'],
            "payment": payment,
            "rating": rating
        })
        print("✅ Trip details saved to history.")

    def show_history(self):
        if not self.ride_history:
            print("\nEmpty History.")
            return
        print("\n--- RIDE HISTORY ---")
        for r in self.ride_history:
            print(f"[{r['date']}] {r['route']} | Rs. {r['fare']:.0f} | ⭐ {r['rating']}/5")
            print(f"   Driver: {r['rider']} | Method: {r['payment']}")

if __name__ == "__main__":
    app = SafarApp()
    app.run()