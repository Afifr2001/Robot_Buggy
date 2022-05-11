from gpiozero import Robot


class CarRobot:
    """
        This is a wraper class of thhe GPIOZERO class 'Robot', that's constructed with two tuples representing the forward and
        backward pins of the left and right controllers respectively, It is also constructed by
        sending an INTEGER of the number of wheels we have. For example,
        if the left motor's controller is connected to GPIOs 4 and 14, while the
        right motor's controller is connected to GPIOs 17 and 18.

        :param integer wheels:
            The number :class:`Integer` of wheels connected to the motors.

        :param tuple gpioInputForMotor1:
            A tuple of two (or three) GPIO pins representing the forward and  
            backward inputs of the left motor's controller. Use three pins if your
            motor controller requires an enable pin.

        :param tuple gpioInputForMotor2:
            A tuple of two (or three) GPIO pins representing the forward and
            backward inputs of the right motor's controller. Use three pins if your
            motor controller requires an enable pin.

        .. attribute:: inputMotor1

            The :tuple:`Tuple` of 2 integers that represent the GPIO ports used for the motor.

        .. attribute:: inputMotor2

            The :tuple:`Tuple` of 2 integers that represent the GPIO ports used for the motor.

        .. attribute:: wheels

            The number :class:`Integer` of wheels connected to the motors.

        .. attribute:: robotInstance

            The :class:`Robot` object from the GPIOZERO library.
        """

    def __init__(self, wheels, gpioInputForMotor1, gpioInputForMotor2):
        self.wheels =  wheels
        # Inputs will represent the GPIOs that are connected to the RPI. In our case, it will
        # take a set of (ID_OF_GPIO1, ID_OF_GPIO2)
        self.inputMotor1 = gpioInputForMotor1
        self.inputMotor2 = gpioInputForMotor2
        self.robotInstance = Robot(left=self.inputMotor1, right=self.inputMotor2)

    def stop(self):
        self.robotInstance.stop()

    def moveForwardFullSpeed(self):
        self.robotInstance.forward(1)

    def moveForwardSlowly(self):
        self.robotInstance.forward(0.5)

    def moveBackwardsFullSpeed(self):
        self.robotInstance.backward(1)

    def moveBackwardsSlowly(self):
        self.robotInstance.backward(0.5)

    def turnLeftFullSpeed(self):
        self.robotInstance.left(1)

    def turnLeftSlowly(self):
        self.robotInstance.left(0.5)

    def turnRightFullSpeed(self):
        self.robotInstance.right(1)

    def turnRightSlowly(self):
        self.robotInstance.right(0.5)