import click
import numpy as np
from numpy import pi
import pandas as pd

#Ik maak hier een groep commando's
@click.group()
def actie():
    pass

@actie.command()
@click.argument("number")
def sin(number):
    """calculates a sin()

    Args:
        number (int): gives the amount of steps
    """    
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@actie.command()
@click.argument("number")
def tan(number):
    """calculates a tan()

    Args:
        number (int): gives the amount of steps
    """    
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# Hier roep ik de groep actie aan
if __name__ == "__main__":
    actie()