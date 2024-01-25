import minimalmodbus
import rmc

class WatLow:
    def __init__(self, addr, baudrate):
        self.address = addr
        self.baudrate = baudrate


controller = WatLow(1, 9600)
# instrument = minimalmodbus.Instrument('COM3', 1, debug=True)  # port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('COM3', controller.address)  # port name, slave address (in decimal)
instrument.serial.baudrate = controller.baudrate;

exit = False

while exit != True:

    print("\nWatLow RMC Interface Terminal\n"
            + "Options\n"
            + "0. Exit\n"
            + "1. Set Modbus RTU Addr (current: " + str(controller.address) + ")\n"
            + "2. Print Analog Input Settings\n"
            + "3. I/O Status\n"
            + "4. Set set-point value\n"
            + "5. Print Analog Input Status\n"
            + "6. Print Monitor Menu\n"
            + "7. Print Limits\n"
            + "8. Print Output Settings\n"
            + "9. Set Output Function\n"
            + "10. Set Control Mode\n")

    opt = int(input("\nEnter Option: "))

    if opt == 0:
        exit = True
    elif opt == 1:
        newAddr = int(input("\nEnter new address (1-16): "))
        controller.address = newAddr
        instrument.address = controller.address
    elif opt == 2:
        rmc.PrintAnalogInputSettings(instrument)
    elif opt == 3:
        rmc.IOstatus(instrument)
    elif opt == 4:
        rmc.SetSP(instrument)
    elif opt == 5:
        rmc.PrintAnalogInputStatus(instrument)
    elif opt == 6:
        rmc.PrintMonitorMenu(instrument)
    elif opt == 7:
        rmc.PrintLimits(instrument)
    elif opt == 8:
        rmc.PrintOutputSettings(instrument)
    elif opt == 9:
        rmc.SetOutputFunction(instrument)
    elif opt == 10:
        rmc.SetControlMode(instrument)
    else:
        print("Invalid option entered")
