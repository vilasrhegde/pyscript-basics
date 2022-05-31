import numpy as np
import random
from utils import add_class


arr = np.array([43,545,565643,4,43])

# pyscript.write('ext',f"External array is {arr}")
arrays = np.array([483,7545,83,443,443])



pyscript.write('shuffle_output',f"{arrays}")


output_el = Element('js_console').element 
output_el.innerHTML = f"{arrays}"



def shuffle_arrays(*args):
    # pyscript.write('shuffle_output','hi')

    shuffled = sorted(arrays,key=lambda k:random.random() )
    pyscript.write('shuffle_output',f"Shuffled array = {shuffled}")

    output_el.innerHTML = f"{arrays}"

    add_class(output_el,"text-blue-500")





