# Abrir y leer el contenido de los archivos Makefile y ble_app_hrs_c_gcc_nrf52.ld
with open('/mnt/data/Makefile', 'r') as file:
    makefile_content = file.read()

with open('/mnt/data/ble_app_hrs_c_gcc_nrf52.ld', 'r') as file:
    ld_script_content = file.read()

makefile_content, ld_script_content
