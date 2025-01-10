# SwimmingPool_MikolajWrobel

## Introduction:
This project aims to make a program that will speed up the billing process.
Program must be easy to use, reliable and reponsive (if needed, reporting human error, so user could correct it).

## File structure:
```
SwimmingPool_MikolajWrobel/
│
├── Pools/ (This folder can be delted is for testing purposes)
│   ├── Maly_Pool_Data
│   │   ├── Cleints.json
│   │   ├── Made_money.json
│   │   ├── Prices.json
│   │   ├── Reservations.json
│   │   └── Working_hours_weekly.json
│   ├── Obrotny_Pool_Data
│   │   ├── Cleints.json
│   │   ├── Made_money.json
│   │   ├── Prices.json
│   │   ├── Reservations.json
│   │   └── Working_hours_weekly.json
|   ├── passwords.json
|   └── Pools.json
│
├── Program/
│   ├── Keyboard_importer.py
│   ├── plotter.py
│   ├── swimming_pool_class.py
│   └── test_classes.py
│
├── README.md
├── requirements.txt
└── To_do.txt
```
## Install
This project requires Python

```bash
git clone git@github.com/decode-debug/SwimmingPool_MikolajWrobel
```

## Run
To run and show the settlement, executes in the Project folder:

```python
python plotter.py
```

Program asks for two types of inputs:
1. Keboard test input
2. Arrow keys input

Program asks for user input in this way:

```
?Swimming_Pool_name
│
?Password (Default: "pipr") -> if inputed incorrectly closes program
│
├── ?Close program -> closes program
│
├── ?Reserve
│    └── questions requered to make reservation
│
├── ?Pay
│    └── questions requered to pay
│
├── ?Plot Finnace Raport
│    └── questions requered to plot payment report
│
└── ?Settings
     ├── ?Change working hours
     │    └── questions requered to Change working hours
     ├── ?Change password
     │    └── questions requered to Change password
     ├── ?Change dicounts
     │    └── questions requered to Change dicounts
     ├── ?Change hourly payment
     │    └── questions requered to Change payment
     ├── ?Change tracks ammount
     │    └── questions requered to Change tracks ammount
     └── ?Create new swimmingpool
          └── questions requered to Change new swimmingpool
```

## Note:
This program has unresolved problem with PyInquirer == 1.0.3, which is  supported up to python 3.9, due to using "mapping".
Though it can be replaced with InquirerPy (for newer versions of python), it will no loger properly validate inputs.


## For Mac users
Never have I used it on mac so have fun :)
