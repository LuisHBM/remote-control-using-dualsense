from dualsense_controller import DualSenseController

class DigitalButtons():
    """
    CallBacks for the buttons:
    
        - Up, Down, Left, Right
        - Cross, Square, Circle, Triangle
        - L1, L2, L3, R1, R2, R3
        - Touchpad click, PlayStation, Mute, Create and Options
        
        (Note: trigger keys can be used analog and digital. L2 and R2 are digital buttons too)
    """
    
    def __init__(self, controller: DualSenseController) -> None:
        self.__controller = controller
        
        self.cross = False
        self.square = False
        self.circle = False
        self.triangle = False
        
        self.up = False
        self.down = False
        self.left = False
        self.right = False
    
    
    def update(self):
        # Cross, Square, Circle, Triangle
        self.cross = self.__controller.btn_cross.pressed
        self.square = self.__controller.btn_square.pressed
        self.circle = self.__controller.btn_circle.pressed
        self.triangle = self.__controller.btn_triangle.pressed
        
        # Up, Down, Left, Right
        self.up = self.__controller.btn_up.pressed
        self.down = self.__controller.btn_down.pressed
        self.left = self.__controller.btn_left.pressed
        self.right = self.__controller.btn_right.pressed
    
    def register_callbacks(self):
        # Cross, Square, Circle, Triangle
        self.__controller.btn_cross.on_down(self.on_cross_btn_pressed)
        self.__controller.btn_square.on_down(self.on_square_btn_pressed)
        self.__controller.btn_circle.on_down(self.on_circle_btn_pressed)
        self.__controller.btn_triangle.on_down(self.on_triangle_btn_pressed)
        
        # Up, Down, Left, Right
        self.__controller.btn_up.on_down(self.on_up_btn_pressed)
        self.__controller.btn_down.on_down(self.on_down_btn_pressed)
        self.__controller.btn_left.on_down(self.on_left_btn_pressed)
        self.__controller.btn_right.on_down(self.on_right_btn_pressed)
    
    # CALLBACKS -----------------------------------------------------------
    
    # Cross, Square, Circle, Triangle
    
    def on_cross_btn_pressed():
        print('Cross button pressed.')
    
    def on_square_btn_pressed():
        print('Square button pressed.')
        
    def on_circle_btn_pressed():
        print('Circle button pressed.')
        
    def on_triangle_btn_pressed():
        print('Triangle button pressed.')
        
    # Up, Down, Left, Right
    
    def on_up_btn_pressed():
        print('Up button pressed.')

    def on_down_btn_pressed():
        print('Down button pressed.')
        
    def on_left_btn_pressed():
        print('Left button pressed.')
        
    def on_right_btn_pressed():
        print('Right button pressed.')
