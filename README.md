- make sure you have Python and Git installed.
- remove evdev from the requirements.txt if the project fails to download packages and try again.

# Cloning
## Linux

```
git clone https://github.com/ant-xy/ATC-Automation.git &&
cd ATC-Automation &&
python3 -m venv .env &&
source .env/bin/activate
```

## Windows

```
git clone https://github.com/ant-xy/ATC-Automation.git && cd ATC-Automation && python -m venv .env && source .env\Scripts\activate
```

# Installation
## Linux
```
python -m pip install -r requirements.txt
```

## Windows
```
python -m pip install -r requirements.txt
```

# Running

```
python main.py
```

# Credits
- the airport database was taken and edited from [OutAirports](https://ourairports.com/data/)
