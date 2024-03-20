import asyncio
import random
import logging
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Configuración del logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Creación del contexto Modbus

Empty_Inverter_Dict = {64: 0, 71: 0, 72: 0, 73: 0, 80: 0, 82: 0, 84: 0, 88: 0, 90: 0, 92: 0, 94: 0, 96: 0, 97: 0, 98: 0, 100: 0,
     102: 0, 104: 0, 106: 0, 108: 0, 110: 0, 118: 0, 122: 0, 123: 0, 74: 0, 126: 0, 128: 0, 130: 0, 132: 0, 138: 0,
     140: 0, 142: 0, 146: 0, 150: 0, 152: 0, 154: 0, 160: 0, 212: 0, 214: 0, 220: 0, 222: 0, 228: 0, 230: 0, 236: 0,
     238: 0, 244: 0, 246: 0, 252: 0, 254: 0, 260: 0, 262: 0, 268: 0, 270: 0, 276: 0, 278: 0, 284: 0, 286: 0, 292: 0,
     294: 0, 300: 0, 302: 0, 308: 0, 310: 0, 316: 0, 318: 0, 324: 0, 326: 0}

Bess_Bibl_SCP = ModbusSparseDataBlock({64: 0})
Bess_Bibl_BatteryMonitor = ModbusSparseDataBlock(
    {64: 0, 70: 0, 72: 0, 74: 0, 76: 0, 88: 0, 90: 0, 94: 0, 96: 0, 106: 0, 108: 0, 110: 0, 112: 0})
Bess_Bibl_Inverter1_Phase1 = ModbusSparseDataBlock(Empty_Inverter_Dict)
Bess_Bibl_Inverter2_Phase2 = ModbusSparseDataBlock(Empty_Inverter_Dict)
Bess_Bibl_Inverter3_Phase3 = ModbusSparseDataBlock(Empty_Inverter_Dict)

slave1 = ModbusSlaveContext(hr=Bess_Bibl_SCP)
slave2 = ModbusSlaveContext(hr=Bess_Bibl_BatteryMonitor)
slave3 = ModbusSlaveContext(hr=Bess_Bibl_Inverter1_Phase1)
slave4 = ModbusSlaveContext(hr=Bess_Bibl_Inverter2_Phase2)
slave5 = ModbusSlaveContext(hr=Bess_Bibl_Inverter3_Phase3)

slaves = {70: slave1, 1: slave2, 12: slave3, 10: slave4, 13: slave5}
context = ModbusServerContext(slaves=slaves, single=False)
async def update_values():
    while True:
        DeviceState = random.choices([random.randint(1, 2), 3, random.randint(
            4, 5), 255], weights=(15, 80, 15, 15), k=1)
        BatteryVoltage = random.randint(-500, 500)
        BatteryCurrent = random.randint(1000, 24300)
        BatteryTemperature = random.randint(23300, 41300)
        BatteryStateOfCharge = random.randint(0, 100)
        BatteryCapacityRemaining = random.randint(0, 100)
        BatteryCapacityRemoved = random.randint(0, 100)
        BatteryTimeToFull = random.randint(0, 360)
        BatteryTimeToDischarge = random.randint(0, 360)
        BatteryCapacityReturned = random.randint(1000, 9000)
        BatteryNumberOfChargeCycles = random.randint(0, 10000)
        BatteryNumberOfDischarges = 10000 - BatteryNumberOfChargeCycles
        InverterEnabled = random.randint(0, 1)
        ChargerEnabled = random.randint(0, 1)
        SellEnabled = random.randint(0, 1)
        BatteryPower = BatteryVoltage * BatteryCurrent
        InverterDCCurrent = random.uniform(0.0, 100.0)
        InverterDCPower = random.uniform(0.0, 10000.0)
        ChargeDCCurrent = random.uniform(0.0, 100.0)
        ChargeDCPower = random.uniform(0.0, 10000.0)
        ChargeDCPowerPercentage = random.uniform(0.0, 100.0)
        GridACFrequency = random.uniform(45.0, 55.0)
        GridACVoltage = random.uniform(190.0, 250.0)
        GridACCurrent = random.uniform(0.0, 100.0)
        GridACPower = random.uniform(0.0, 10000.0)
        GridACInputPowerApparent = random.uniform(0.0, 10000.0)
        GridACInputCurrent = random.uniform(0.0, 100.0)
        GridACInputVoltage = random.uniform(190.0, 250.0)
        GridACL1Voltage = random.uniform(190.0, 250.0)
        GridACL1Current = random.uniform(0.0, 100.0)
        InverterStatus = random.randint(0, 1)
        ChargerStatus = random.randint(0, 1)
        ForcedSell = random.randint(0, 2)
        GridOutputVoltage = random.uniform(190.0, 250.0)
        GridOutputCurrent = random.uniform(0.0, 100.0)
        GridOutputFrequency = random.uniform(45.0, 55.0)
        GridOutputPower = random.uniform(0.0, 10000.0)
        GridOutputPowerApparent = random.uniform(0.0, 10000.0)
        LoadACVoltage = random.uniform(190.0, 250.0)
        LoadACL1Voltage = random.uniform(190.0, 250.0)
        LoadACL1Current = random.uniform(0.0, 100.0)
        LoadACCurrent = random.uniform(0.0, 100.0)
        LoadACFrequency = random.uniform(45.0, 55.0)
        LoadACPower = random.uniform(0.0, 10000.0)
        LoadACPowerApparent = random.uniform(0.0, 10000.0)
        EnergyFromBatteryDay = random.uniform(0.0, 10000.0)
        BatteryDischargeActiveDay = random.uniform(0.0, 24.0)
        EnergyFromBatteryMonth = random.uniform(0.0, 300000.0)
        BatteryDischargeActiveMonth = random.uniform(0.0, 720.0)
        BatteryDischargeActive = random.uniform(0.0, 8760.0)
        EnergyToBatteryDay = random.uniform(0.0, 10000.0)
        BatteryChargeActiveDay = random.uniform(0.0, 24.0)
        EnergyToBatteryMonth = random.uniform(0.0, 300000.0)
        BatteryChargeActiveMonth = random.uniform(0.0, 720.0)
        EnergyFromBattery = random.uniform(0.0, 1000000.0)
        EnergyToBattery = random.uniform(0.0, 1000000.0)
        BatteryChargeActive = random.uniform(0.0, 8760.0)
        GridInputEnergyDay = random.uniform(0.0, 10000.0)
        GridInputActiveDay = random.uniform(0.0, 24.0)
        GridInputEnergyMonth = random.uniform(0.0, 300000.0)
        GridInputActiveMonth = random.uniform(0.0, 720.0)
        GridInputEnergy = random.uniform(0.0, 1000000.0)
        GridInputActive = random.uniform(0.0, 8760.0)
        GridOutputEnergyDay = random.uniform(0.0, 10000.0)
        GridOutputActiveDay = random.uniform(0.0, 24.0)
        GridOutputEnergyMonth = random.uniform(0.0, 300000.0)
        GridOutputActiveMonth = random.uniform(0.0, 720.0)
        GridOutputEnergy = random.uniform(0.0, 1000000.0)
        GridOutputActive = random.uniform(0.0, 8760.0)
        LoadOutputEnergyDay = random.uniform(0.0, 10000.0)
        LoadOutputActiveDay = random.uniform(0.0, 24.0)
        LoadOutputEnergyMonth = random.uniform(0.0, 300000.0)
        LoadOutputActiveMonth = random.uniform(0.0, 720.0)
        LoadOutputEnergy = random.uniform(0.0, 1000000.0)
        LoadOutputActive = random.uniform(0.0, 8760.0)
