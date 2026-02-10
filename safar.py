import time
import heapq

class SafarApp:
    def __init__(self):
        # Everything inside the class is indented 4 spaces
        # Everything inside a function is indented 8 spaces
        self.cities_graph = {
            'Karachi': {'Hyderabad': 160, 'Thatta': 100},
            'Hyderabad': {'Karachi': 160, 'Sukkur': 330, 'Mirpur Khas': 75, 'Dadu': 180},
            'Mirpur Khas': {'Hyderabad': 75},
            'Thatta': {'Karachi': 100, 'Badin': 100},
            'Badin': {'Thatta': 100, 'Hyderabad': 110},
            'Sukkur': {'Hyderabad': 330, 'Multan': 440, 'Larkana': 95, 'Quetta': 390},
            'Larkana': {'Sukkur': 95, 'Dadu': 130},
            'Dadu': {'Larkana': 130, 'Hyderabad': 180},
            'Quetta': {'Sukkur': 390, 'Ziarat': 120, 'Sibi': 160},
            'Ziarat': {'Quetta': 120},
            'Sibi': {'Quetta': 160},
            'Multan': {'Sukkur': 440, 'Bahawalpur': 95, 'Sahiwal': 170},
            'Bahawalpur': {'Multan': 95},
            'Sahiwal': {'Multan': 170, 'Lahore': 180},
            'Lahore': {'Sahiwal': 180, 'Gujranwala': 95, 'Faisalabad': 180},
            'Gujranwala': {'Lahore': 95},
            'Faisalabad': {'Lahore': 180},
            'Islamabad': {'Rawalpindi': 15, 'Abbottabad': 120},
            'Abbottabad': {'Islamabad': 120},
            'Rawalpindi': {'Islamabad': 15, 'Jhelum': 120, 'Peshawar': 170},
            'Jhelum': {'Rawalpindi': 120},
            'Peshawar': {'Rawalpindi': 170},
        }

        self.riders = [
            {"name": "Ahmed Ali", "phone": "0321-4567890", "plate": "LEC-4567"},
            {"name": "Zubair Khan", "phone": "0300-9876543", "plate": "RI-229"},
            {"name": "M. Usman", "phone": "0333-1122334", "plate": "KHI-8801"},
            {"name": "Faisal Shah", "phone": "0312-5566778", "plate": "MN-442"},
        ]

        self.vehicles = {"Bike": 15, "Mini Car": 35, "Ac Car": 60}
        self.ride_history = []

    def dijkstra(self, start, end):
        distances = {city: float('inf') for city in self.cities_graph}
        previous = {city: None for city in self.cities_graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            curr_dist, curr_city = heapq.heappop(pq)
            if curr_city == end:
                path = []
                while curr_city:
                    path.insert(0, curr_city)
                    curr_city = previous[curr_city]
                return path, distances[end]

            if curr_dist > distances[curr_city]:
                continue

            for neighbor, weight in self.cities_graph[curr_city].items():
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = curr_city
                    heapq.heappush(pq, (new_dist, neighbor))
        return None, float('inf')

    def run(self):
        while True:
            print("\n" + "=" * 30)
            print("      SAFAR RIDE-HAILING")
            print("=" * 30)
            print("1. Book a Ride\n2. View History\n3. Emergency\n4. Exit")
            choice = input("Select Option: ")
            if choice == '1': 
                self.handle_booking()
            elif choice == '2': 
                self.show_history()
            elif choice == '3': 
                print("\n🚨 Emergency: Call 15")
            elif choice == '4': 
                print("Exiting... Safe travels!")
                break

    def handle_booking(self):
        print("\nAvailable Cities:", ", ".join(sorted(self.cities_graph.keys())))
        start = input("Pickup City: ").strip().title()
        end = input("Destination: ").strip().title()

        if start not in self.cities_graph or end not in self.cities_graph:
            print("❌ Invalid city name.")
            return

        path, dist = self.dijkstra(start, end)
        if not path:
            print("❌ No route found.")
            return

        print(f"\n📍 Route: {' -> '.join(path)}")
        print(f"📏 Distance: {dist} km")

        vehicle = input("Choose (Bike / Mini Car / Ac Car): ").strip().title()
        if vehicle in self.vehicles:
            fare = dist * self.vehicles[vehicle]
            print(f"💰 Total Fare: Rs. {fare:.0f}")
            self.simulate_ride(start, end, vehicle, fare)
        else:
            print("❌ Invalid vehicle choice.")

    def simulate_ride(self, start, end, vehicle, fare):
        rider = random.choice(self.riders)
        print(f"👤 Rider Assigned: {rider['name']} ({rider['plate']})")
        time.sleep(1) # Simulating a short delay
        rating = input("Rate your experience (1-5): ")
        self.ride_history.append({
            "date": time.ctime(), 
            "route": f"{start} to {end}", 
            "fare": fare, 
            "rating": rating
        })
        print("✅ Ride completed.")

    def show_history(self):
        if not self.ride_history:
            print("\n📜 No ride history found.")
            return
        print("\n--- Ride History ---")
        for r in self.ride_history:
            print(f"{r['date']} | {r['route']} | Rs. {r['fare']} | ⭐ {r['rating']}")

# The entry point must NOT be indented
if __name__ == "__main__":
    app = SafarApp()
    app.run()