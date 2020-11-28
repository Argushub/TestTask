import json_validate
import json_to_schema_validate
import os


def validate(data, schema, schema_name, data_name):
    des_data = json_validate.json_deserialize(data, file_name=data_name)
    des_schema = json_validate.json_deserialize(schema, file_name=schema_name)
    json_to_schema_validate.required_field_validate(schema=des_schema, data=des_data, schema_name=schema_name, data_name=data_name)
    json_to_schema_validate.properties_field_validate(schema=des_schema, data=des_data, schema_name=schema_name, data_name=data_name)


for schema_name in os.listdir(path='task_folder/schema'):
    schema_path = "task_folder/schema/"+schema_name
    schema_file = open(schema_path)
    schema = schema_file.read()
    for data_name in os.listdir(path='task_folder/event'):
        data_path = "task_folder/event/"+data_name
        data_file = open(data_path)
        data = data_file.read()
        validate(data=data, schema=schema, schema_name=schema_name, data_name=data_name)
        data_file.close()
    schema_file.close()


