import log
from list_property_validate import property_list_validate
from str_property_validate import property_str_validate


def required_field_validate(schema, data, data_name, schema_name):
    validation = True
    if "required" in schema.keys():
        required_fields = schema["required"]
        for required_field in required_fields:
            if isinstance(data, dict):
                if required_field not in data.keys():
                    log.logging.error("В файле {} не найдено обязательное поле {}, \
    которое требуется в схеме {}".format(data_name, required_field, schema_name))
                    validation = False
                else:
                    log.logging.info("File {} with schema {} has field {} and its OK".format(data_name, schema_name, required_field))
            else:
                log.logging.error("Неверный формат JSON файла {}". format(data_name))
    return validation


def properties_field_validate(schema, data, data_name, schema_name):
    validation = True
    if "properties" in schema.keys():
        properties_fields = schema["properties"]
        if isinstance(data, dict):
            for data_key in data.keys():
                if data_key not in properties_fields:
                    log.logging.error('В файле {} поле {} не описано в properties JSON-схемы {}, проверьте написание \
или удалите его'.format(data_name, data_key, schema_name))
                    validation = False
                else:
                    if isinstance(properties_fields[data_key]["type"], str):
                        validation = property_str_validate(properties_fields[data_key]["type"], data[data_key], \
                                                           data_key, schema, data_name, schema_name)
                    elif isinstance(properties_fields[data_key]["type"], list):
                        validation = property_list_validate(properties_fields[data_key]["type"], data[data_key], \
                                                            data_key, schema, data_name, schema_name)
                    else:
                        log.logging.error('В поле "properties" схемы {} значение {} должно быть записано в виде \
"%название%": {{"type": %тип данных%}} или "%название%": {{"type": [%тип данных1%, %тип данных2%, \
и так далее]}}'.format(schema_name, data_key))
                    validation = False
    return validation
