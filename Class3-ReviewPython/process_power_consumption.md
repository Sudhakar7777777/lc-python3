# Notes on how to run the script

- Syntax: process_power_consumption.py <start date> <end date> <AM/PM/2M> <in file name> <out file name>
- Date format: dd/mm/yyyy

## Commands:

- /opt/anaconda3/bin/python ./process_power_consumption.py 26/11/2007 27/11/2007 AM household_power_consumption.txt out.txt
- /opt/anaconda3/bin/python ./process_power_consumption.py 26/11/2007 27/11/2007 PM household_power_consumption.txt out.txt
- /opt/anaconda3/bin/python ./process_power_consumption.py 26/11/2007 27/11/2007 2M household_power_consumption.txt out.txt

## Invalid Commands:

- /opt/anaconda3/bin/python ./process_power_consumption.py
- /opt/anaconda3/bin/python ./process_power_consumption.py help
