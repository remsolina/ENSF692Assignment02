# input_processing.py
# Remi Oyediji, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.



# Creates a Sensor class for use in executing the program in Main.
class Sensor:

    # Defines the constructor to initialize the use of the Sensor class for car detections
    # Defines variables to be detected by a car
    def __init__(self):
        
        traffic_light = "green"
        pedestrian = "no"
        vehicle = "no"

        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self.vehicle = vehicle


    # Defines a function for updating the status of Traffic Light, and if Pedestrian & Vehcile is detected
    def update_status(self, color, pstatus, vstatus): # Adds required arguments for updating the function
        
        if color in ["green", "yellow", "red"]:
            self.traffic_light = color
        else:
            print("Invalid vision change")
            
        if pstatus in ["yes", "no"]:
            self.pedestrian = pstatus
        else:
            print("Invalid vision change")
            
        if vstatus in ["yes", "no"]:
            self.vehicle = vstatus
        else:
            print("Invalid vision change")

# Prints relative action message and current status based on user input, and using the sensor object
def print_message(sensor):
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")

    elif sensor.traffic_light == "green":
       print("\nProceed\n")

    elif sensor.traffic_light == "yellow":
        print("\nCaution\n")
    
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")
    print("\n")
    

# Defines main function for executing the Vision Dectection Program
def main():
    sensor = Sensor()
    # Uses the while loop to keep options open till user closes the program
    while True:
        try:
            print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
            print("Are changes detected in the vision input?")
            choice = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))

            if choice == 0:
                break
            elif choice == 1:
                color = input("What change has been identified: ").strip()
                sensor.update_status(color, sensor.pedestrian, sensor.vehicle)
            elif choice == 2:
                pstatus = input("What change has been identified: ").strip()
                sensor.update_status(sensor.traffic_light, pstatus, sensor.vehicle)
            elif choice == 3:
                vstatus = input("What change has been identified: ").strip()
                sensor.update_status(sensor.traffic_light, sensor.pedestrian, vstatus)
            
        except ValueError:
            print(f"You must select either 1, 2, 3, or 0")

        else: 
            print_message(sensor)
        
        
# Conventional Python code for running main within a larger program
if __name__ == '__main__':
    main()

