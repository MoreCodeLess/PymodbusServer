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
