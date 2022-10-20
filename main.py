# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import user_interface as ui
import crud

crud.init_data_base('base_phone.csv')
ui.ls_menu()