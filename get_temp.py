import sys
import configparser
import pymodbus.exceptions
from pymodbus.client.sync import ModbusTcpClient


def get_sensor_readings(client, reg_address, reg_count, slave_id):
    host_response = client.read_holding_registers(
        int(reg_address), int(reg_count), unit=int(slave_id)
    )
    sensor_readings = tuple(
        round(register/100, 1) for register in host_response.registers
    )
    return sensor_readings


def main():
    config_file = 'config.ini'
    config = configparser.ConfigParser()
    config.read(config_file)
    host = config['modbus_host']['host']
    port = config['modbus_host']['port']
    reg_address = config['register']['address']
    reg_count = config['register']['count']
    slaves_id_collection = config['slave_id'].items()
    client = ModbusTcpClient(host=host, port=port)
    for name, slave_id in slaves_id_collection:
        try:
            sensor_readings = get_sensor_readings(
                client, reg_address, reg_count, slave_id
            )
        except pymodbus.exceptions.ConnectionException:
            print('Check [modbus_host] config section in config.ini')
            sys.exit(1)
        else:
            print(sensor_readings)
        finally:
            client.close()


if __name__ == '__main__':
    main()
