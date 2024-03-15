import pandas as pd
from pathlib import Path 
import requests

# Download helper functions from Learn PyTorch repo (if not already downloaded)
if Path("helper_functions.py").is_file():
  print("helper_functions.py already exists, skipping download")
else:
  print("Downloading helper_functions.py")
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)

if Path("data/ec_data.csv").is_file():
  print("helper_functions.py already exists, skipping download")
else:
  print("Downloading helper_functions.py")
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)



DATA_PATH = Path("data")
FILE_NAME = "eb_pandas.csv"
FILE_SAVE_PATH = DATA_PATH / FILE_NAME



# MODEL_PATH = Path("models")
# MODEL_PATH.mkdir(parents=True, # create parent directories if needed
#                  exist_ok=True # if models directory already exists, don't error
# )

# # Create model save path
# MODEL_NAME = "03_pytorch_computer_vision_model_2.pth"
# MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME
