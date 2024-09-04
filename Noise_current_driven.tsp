buf1 = buffer.make(2000000)
--Set up measure function
smu.measure.func =smu.FUNC_DC_VOLTAGE
smu.measure.terminals = smu.TERMINALS_REAR
smu.measure.nplc = 0.1
smu.measure.autorange = smu.ON
smu.measure.autozero.enable = smu.OFF
smu.source.readback = smu.OFF
--Set up source function
smu.source.func = smu.FUNC_DC_CURRENT
smu.source.vlimit.level = 3
smu.source.level = 2e-6
smu.source.highc = smu.OFF

--Turn on output and initiate readings
smu.source.output = smu.ON

trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_001.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 5e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_002.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 7e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_003.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 10e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_004.csv", buffer.SAVE_RELATIVE_TIME)


buf1.clear()

smu.source.level = 15e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_005.csv", buffer.SAVE_RELATIVE_TIME)


buf1.clear()


smu.source.level = 20e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_006.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()


smu.source.level = 30e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_007.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 40e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_008.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 50e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_009.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 60e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_010.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 70e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_011.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 80e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_012.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 90e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_013.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 100e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_014.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 150e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_015.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 200e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_016.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 300e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_017.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 400e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_018.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 500e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_019.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 600e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_020.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 700e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_021.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 800e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_022.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 900-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_023.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1000e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_024.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1100e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_025.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1200e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_026.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1300e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_027.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1400e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_028.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1500e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_029.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1600e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_030.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1700e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_031.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1800e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_032.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 1900e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_033.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()

smu.source.level = 2000e-6
trigger.model.load("SimpleLoop", 1500000,0,buf1)
trigger.model.initiate()
waitcomplete()
buffer.save(buf1, "/usb1/it_034.csv", buffer.SAVE_RELATIVE_TIME)

buf1.clear()



smu.source.output = smu.OFF