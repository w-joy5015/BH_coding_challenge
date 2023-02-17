from DAG_runner import main
import io
import sys
import time

def test_DAG_runner_prints_values_in_correct_order():
    """
        This tests that the DAG_runner outputs the node values 
        in the correct order and within the expected timeframe.
    """
    output = io.StringIO()
    sys.stdout = output
    main(["DAG_1.json"])
    time.sleep(6)
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "A\nB\nC\nD\nE\n"