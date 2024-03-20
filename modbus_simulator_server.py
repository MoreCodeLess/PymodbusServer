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
