import json

def json_to_dict_converter(DAG_json:str) -> dict:
    with open(DAG_json) as json_file:
        return json.load(json_file)

def find_starting_node(DAG_dict:dict[str, dict]) -> str:
    for node_name, node_info in DAG_dict.items():
        if node_info.get("start")==True:
            return node_name