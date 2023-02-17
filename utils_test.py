from utils import json_to_dict_converter, find_starting_node

def test_json_to_dict_converter():
    expected_dict = json_to_dict_converter("DAG_1.json")
    assert type(expected_dict) is dict

def test_find_starting_node():
    test_DAG_dict = {
        "B": {"edges": {"D": 1}},
        "C": {"edges": {"D": 3}},
        "D": {"edges": {"E": 2}},
        "A": {"start":True, "edges": {"B": 2, "C":3}},
        "E": {"edges": {}}
    }
    assert find_starting_node(test_DAG_dict) == "A"