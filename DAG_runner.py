import threading
import time
import sys
from utils import json_to_dict_converter, find_starting_node

def main(args):
    """
        Args: a JSON file representing a directional acyclic graph (DAG)
        Returns: null

        This script takes a DAG and outputs values beginning at the starting node,
        and travels along the graph using multithreading. The values are output to
        the console on a timer, based on values of the edges that represent a wait
        time in seconds.
    """
    # Pass a json file as an argument. This will be converted to a dict.
    DAG_dict=json_to_dict_converter(args[0])

    def wait_then_travel(next_node_name: str, wait_time: int):
        """
            This function pauses on the current thread it is on for the given wait time.
            It then gets the next node from the DAG_dict and invokes visit().
        """
        time.sleep(wait_time)
        next_node_info = DAG_dict.get(next_node_name)
        visit_node(next_node_name, next_node_info)

    def visit_node(node_name: str, node_info: dict[str,dict]):
        """
            This function checks if the current node has been visited before. If not, it
            prints the node name and flags the node as being visited. It then invokes
            wait_then_travel() on all the edges connected to the current node and has them
            each run on a new thread.
        """
        if node_info.get("visited") != True:
            print(node_name)
            # Uncomment below line to see time elapsed from when the first values prints
            # print (time.time()-start)
        node_info["visited"] = True
        for next_node_name, wait_time in node_info["edges"].items():
            t = threading.Thread(target=wait_then_travel, args=(next_node_name, wait_time))
            t.start()

    starting_node = find_starting_node(DAG_dict)
    # Uncomment below line to see time elapsed from when the first values prints
    # start = time.time()
    visit_node(starting_node, DAG_dict[starting_node])

if __name__=="__main__":
    main(sys.argv[1:])