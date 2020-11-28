import log
import json_to_schema_validate


def property_str_validate(type, value, key, schema, data_name, schema_name):
    validation = False
    if type == "integer":
        if not isinstance(value, int):
            log.logging.error("Тип значения в JSON файле {} в поле {} по \
схеме {} должен быть {}".format(data_name, key, schema_name, type))
        else:
            log.logging.info("{} type {} is OK".format(key, type))
            validation = True
    elif type == "string":
        if not isinstance(value, str):
            log.logging.error("Тип значения в JSON файле {} в поле {} по \
схеме {} должен быть {}".format(data_name, key, schema_name, type))
        else:
            log.logging.info("{} type {} is OK".format(key, type))
            validation = True
    elif type == "null":
        if value is not None:
            log.logging.error("Тип значения в JSON файле {} в поле {} по \
схеме {} должен быть {}".format(data_name, key, schema_name, type))
        else:
            log.logging.info("{} type {} is OK".format(key, type))
            validation = True
    elif type == "object":
        if isinstance(value, dict):
            child_data_name = data_name+':'+key
            if json_to_schema_validate.required_field_validate(schema["properties"][key], value, child_data_name, schema_name) and \
               json_to_schema_validate.properties_field_validate(schema["properties"][key], value, child_data_name, schema_name):
                validation = True
                log.logging.info("{} type {} is OK".format(key, type))
    else:
        log.logging.error("Тип значения в JSON файле {} в поле {} должен быть string, null, integer \
или object".format(data_name, key))
    return validation
