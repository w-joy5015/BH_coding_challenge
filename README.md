# BigHat Coding Challenge - DAG Runner
`DAG_runner.py` is a script that can be run with a given directed acyclic graph (DAG) formatted as a .json file. It meets the following criteria:

1. Runner accepts a DAG in .json format.
2. Runner prints the node values of each node it visits, beginning with the designated starting node. It continues printing in order based on direction and wait time determined by the edges connecting nodes.
3. Runner processes nodes in parallel using multithreading. If a node has already been printed, it does not print out the node again.

## Setup and how to use
1. Create and activate a virtualenv. Then install requirements.txt
2. `DAG_runner` accepts a .json file as a command line argument. As an example, to run it on `DAG_1.json` use:
```bash
python DAG_runner.py DAG_1.json
```
You can also replace DAG_1.json with any path to a DAG in json format.

3. [optional] To see the time elapsed between node values as they print out, uncomment out lines 28 and 36 and run step 2 again. Note that uncommenting these lines out will make one of the unit tests fail since the unit test checks the console output.

## How to run tests
1. Run `pytest`. There are currently 3 unit tests: 2 from `untils_test.py` and 1 from `DAG_runner_test.py`.
2. *Note:* `DAG_runner_test.py` is dependant on `DAG_1.json` for testing, so changes made to one may also need to be reflected in the other.
