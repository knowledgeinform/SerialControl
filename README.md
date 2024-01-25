# SerialControl

To find available serial ports on windows computer:
python -m serial.tools.list_ports -v

For Watlow control: an output must be:
1. Connected to the proper driving function (e.g. Heat Power)
2. Connected to the proper *instance* of that driving function
  For example, to have the thermocouple on the 2nd input (2nd instance of analog-input/2nd instance of PID control loop), the output function for the 3rd instance (corresponding to slot B) must be set to the proper driving function (easy), and also the proper instance:
  write_register(1030 + 30*2, 2)
  Note that last 2 is critically important because the default value for these registers is 1 (which means all the outputs look at the same input coming from the 1st instance of Heat Power [i.e. input 1, on slot A])
