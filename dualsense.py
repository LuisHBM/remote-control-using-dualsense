from dualsense_controller import DualSenseController, DeviceInfo

from components.battery import Battery
from components.digital_buttons import DigitalButtons
from components.analog_buttons import AnalogButtons

from time import sleep


class DualSenseHandler():
    
    MIN_BATTERY_LEVEL = 20

    def __init__(self, device_index: int = 0) -> None:
        """
        DualSenseHandler class constructor

        Args:
            device_index (int, optional): Device index on the device_info list. Defaults to 0.

        Raises:
            Exception: device_index arg is not a int
        """
        if not isinstance(device_index, int):
            raise Exception(f"Error while init DualSenseHandler: type {type(device_index)} for device_index is not valid.")

        # Dualsense info
        self.controller_index = device_index
        self.device_info = self.__get_device_info()
        self.controller: DualSenseController = None
        
        # Detecting and initializing controller
        self.__try_connect()
        self.is_running = True
        
        # Components
        self.battery = Battery(self.controller)
        self.digital_buttons = DigitalButtons(self.controller)
        self.analog_buttons = AnalogButtons(self.controller)
        
        self.__register_callbacks()
    
    # METHODS -------------------------------------------------------------------------------------------
    
    def to_string(self):
        return ("DIGITAL VALUES==================\n"
                f"Cross: {self.digital_buttons.cross}\n"
                f"Square: {self.digital_buttons.square}\n"
                f"Circle: {self.digital_buttons.circle}\n"
                f"Triangle: {self.digital_buttons.triangle}\n"
                f"Up: {self.digital_buttons.up}\n"
                f"Down: {self.digital_buttons.down}\n"
                f"Left: {self.digital_buttons.left}\n"
                f"Right: {self.digital_buttons.right}\n"
                "ANALOG VALUES===================\n"
                f"Left Stick: {self.analog_buttons.left_stick}\n"
                f"Right Stick: {self.analog_buttons.right_stick}\n"
                f"L2: {self.analog_buttons.L2}\n"
                f"R2: {self.analog_buttons.R2}"
                )
        
    def __get_device_info(self) -> DeviceInfo:
        """
        Gets the device info corresponding to the device index.

        Raises:
            Exception: failed to find the device info on the device_infos list.

        Returns:
            DeviceInfo: the corresponding device info.
        """
        devices_info = DualSenseController.enumerate_devices()
        
        if devices_info:
            
            if not len(devices_info) < self.controller_index:
                return devices_info[self.controller_index]
            
            raise Exception(f"Error while getting device info: device of index {self.controller_index} not found.")
        
        raise Exception(f"Error while getting device info: no device detected.")
    
    
    def __try_connect(self) -> None:
        """
        Tries to connect to the device.

        Raises:
            Exception: self.device_info is None
        """
        if not self.device_info:
            raise Exception('Error while trying to connect: no DualSense controller detected.')
        else:
            self.controller = DualSenseController(device_index_or_device_info=self.device_info)
          
            
    def __register_callbacks(self) -> None:
        pass
        #self.battery.register_callbacks()
        #self.digital_buttons.register_callbacks()


    def __update_states(self) -> None:
        
        self.battery.update()
        self.digital_buttons.update()
        self.analog_buttons.update()

    
    def loop(self) -> None:
        self.controller.activate()
        
        while self.is_running:
            sleep(0.001)
            self.__update_states()
            print(self.to_string())
            print(" ")
            
        self.controller.deactivate()
    
    def stop(self) -> None:
        self.is_running = False


if __name__ == "__main__":
    
    device_index = 0
    ds_handler = DualSenseHandler(device_index)
    ds_handler.loop()
    
    
    