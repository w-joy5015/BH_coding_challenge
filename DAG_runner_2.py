import json
import threading
import time

def json_to_dict_converter(DAG_json:str) -> dict:
    with open(DAG_json) as json_file:
        return json.load(json_file)

def find_starting_node(DAG_dict):
    for node_name, node_info in DAG_dict.items():
        if node_info.get("start")==True:
            return node_name

if __name__=="__main__":
    DAG_dict=json_to_dict_converter("DAG_1.json")

    def wait_then_travel(next_node_name, wait_time):
        time.sleep(wait_time)
        next_node_info = DAG_dict.get(next_node_name)
        visit_node(next_node_name, next_node_info)

    def visit_node(node_name: str, node_info: dict[str,dict]):
        if node_info.get("visited") != True:
            print(node_name)
        node_info["visited"] = True
        for next_node_name, wait_time in node_info["edges"].items():
            t = threading.Thread(target=wait_then_travel, args=(next_node_name, wait_time))
            t.start()

    starting_node = find_starting_node(DAG_dict)
    visit_node(starting_node, DAG_dict[starting_node])