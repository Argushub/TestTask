import log
import json_to_schema_validate


def property_list_validate(types_list, value, key, schema, data_name, schema_name):
    type_valid = False
    for type in types_list:
        if type == "integer":
            if isinstance(value, int):
                type_valid = True
                log.logging.info("{} type {} is OK".format(key, type))
        elif type == "string":
            if isinstance(value, str):
                type_valid = True
                log.logging.info("{} type {} is OK".format(key, type))
        elif type == "null":
            if value is None:
                type_valid = True
                log.logging.info("{} type {} is OK".format(key, type))
        elif type == "object":
            child_data_name = data_name+':'+key
            if isinstance(value, dict):
                if json_to_schema_validate.required_field_validate(schema["properties"][key], value) and \
                   json_to_schema_validate.properties_field_validate(schema["properties"][key], value):
                    type_valid = True
                    log.logging.info("{} type {} is OK".format(key, type))
        else:
            log.logging.error("Тип значения в JSON файле {} в поле {} должен быть string, \
null, integer или object".format(data_name, key))
    if not type_valid:
        log.logging.error("Тип значения в JSON файле {} в поле {} по схеме {} должен быть \
одним из следующих типов: {}".format(data_name, key, schema_name, types_list))
    else:
        log.logging.info("{} is OK".format(types_list))
    return type_valid
