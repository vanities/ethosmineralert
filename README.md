# ethosmineralert
alerts when my miner turns off and tells me stats every ~morning~ ~hour~ 4 hours.

Set a schedule:
```
crontab -e
0 0,4,8,12,16,20 * * * * python3 /path/to/main.py
```

