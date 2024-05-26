from dualsense_controller import DualSenseController

class Battery():
    """
    CallBacks for the battery:
    
    """
    
    def __init__(self, controller: DualSenseController) -> None:
        self.__battery = controller.battery
        self.value = 0
    
    def register_callbacks(self):
        self.__battery.on_change(self.on_battery_change)
        self.__battery.on_lower_than(20, self.on_battery_lower_than)
        self.__battery.on_charging(self.on_battery_charging)
        self.__battery.on_discharging(self.on_battery_discharging)
        
    def update(self):
        self.value = self.__battery.value
    
    # CALLBACKS -----------------------------------------------------------
    
    def on_battery_change(battery) -> None:
        print(f'Battery Level: {battery}%')

    def on_battery_lower_than(battery_level) -> None:
        print(f'ATTENTION! Battery low: {battery_level}%')

    def on_battery_charging(battery_level) -> None:
        print(f'Charging... {battery_level}%')

    def on_battery_discharging(battery_level) -> None:
        print(f'Discharging... {battery_level}%')