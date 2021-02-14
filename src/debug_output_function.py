from rich.console import Console

import pandas as pd

cs = Console()

data = pd.DataFrame({'Column1': [1,2], 'Column2': [3,4]})

def function1():
    global data
    cs.log(data, log_locals=True)

function1()