# Project set up

* Project contains data folder with all needed data
* EDA folder with jupyter notebook of EDA
* Model folder for storing model
* src for all needed scripts


# EDA

For research install EDA requirements

```
pip install -r requirements-eda.txt
```

# Training/inference

## Requirements:
```
pip install -r requirements.txt
```
Train:
```
python src/train.py
```
Inference (Require model in `model/model.pkl`)
```
python src/inference.py
```

