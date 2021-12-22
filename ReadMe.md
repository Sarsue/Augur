Getting Started
Install

Our current recommendation is to use this project with Anaconda's Python distribution - either full Anaconda3 Latest or Miniconda3 Latest. 

Install Anaconda
Confirm that you have it with: conda -V. The output should be something along the lines of: conda 4.9.2

Create Environment
You can name the environment whatever you want. Although I use augur

conda create -n augur 
Activate the virtual environment
conda activate augur
Note: At the end, you can deactivate it with: conda deactivate

Fork the Project
Via HTTPS: git clone https://github.com/Sarsue/Augur.git
via SSH: git clone git@https://github.com/Sarsue/Augur.git

pip install -r requirements.txt

Navigate into the folder with: cd augur/src

python3 augur.py


