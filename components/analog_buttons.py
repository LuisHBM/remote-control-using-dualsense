from dualsense_controller import DualSenseController

class AnalogButtons():
    """
    CallBacks for the buttons:
    
        - Two analog sticks
        - Two analog triggers (L2 and R2)
        
        (Note: (Note: trigger keys can be used analog and digital. L2 and R2 are digital buttons too))
    """
    
    def __init__(self, controller: DualSenseController) -> None:
        self.__controller = controller
        
        self.left_stick = 0.
        self.right_stick = 0.
        
        self.L2 = 0.
        self.R2 = 0.
        
        
    def update(self):
        self.left_stick = self.__controller.left_stick.value
        self.right_stick = self.__controller.right_stick.value
        
        self.L2 = self.__controller.left_trigger.value
        self.R2 = self.__controller.right_trigger.value
    
    
    def register_callbacks(self):
        self.__controller.left_trigger.on_change(self.on_left_trigger)
        self.__controller.left_stick_x.on_change(self.on_left_stick_x_changed)
        self.__controller.left_stick_y.on_change(self.on_left_stick_y_changed)
        self.__controller.left_stick.on_change(self.on_left_stick_changed)
        
        self
    
    # CALLBACKS -----------------------------------------------------------
    
    def on_left_trigger(value):
        print(f'Left trigger changed: {value}')


    def on_left_stick_x_changed(left_stick_x):
        print(f'Left Stick X: {left_stick_x}')


    def on_left_stick_y_changed(left_stick_y):
        print(f'Left Stick Y: {left_stick_y}')


    def on_left_stick_changed(left_stick):
        print(f'on_left_stick_changed: {left_stick}')
