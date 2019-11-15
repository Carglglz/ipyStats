## ipyStats : python bindings to istats



***Requirements***:

* istats (http://chris911.github.io/iStats/)



***Install***:

```
git clone https://github.com/Carglglz/ipyStats.git
cd ipyStats
pip install .
```



***Usage example:***

```python
from ipyStats import istat

istat.cpu_temp()
{'CPU temp': '40.81°C'}

istat.batt_time()
{'Battery time remaining': 'Unlimited'} ## This means is charger is connected

istat.batt_charge()
{'Battery charge': '100%'}

 istat.palmr_temp()
{'palmr_temp': '27.56 ºC'}

istat.fan_speed()
{'Fan 0 speed': '0 RPM', 'Fan 1 speed': '0 RPM'}

istat.batt_temp()
{'Battery temp': '31.5°C'}

istat.batt_time()
{'Battery time remaining': '5:23'}
```

