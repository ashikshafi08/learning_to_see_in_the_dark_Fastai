import subprocess
import sys

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rawpy"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fastbook"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "PIL"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pathlib"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fastai"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "random"])
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "os"])
