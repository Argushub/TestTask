import json
import log


def json_deserialize(json_data, file_name):
    try:
        new_data = json.loads(json_data)
    except Exception as e:
        log.logging.exception("Ошибка записи JSON логики внутри файла {} в строке {},\
символе {}".format(file_name, e.lineno, e.pos))
        return False
    else:
        return new_data
