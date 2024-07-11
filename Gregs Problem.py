
import pandas as pd
import matplotlib.pyplot as plt
#from datetime import datetime



df1 = pd.read_csv("/Users/marinamudrova/Downloads/001_1(CYC2)_UPDATED.csv")
xde1 = df1['TestTime']
xde2 = df1['TestTime']
yde1 = df1['Voltage']

#def convert_to_seconds(xde1):
#   if "-" not in xde1:
#       hours, minutes, seconds = map(int, xde1.split(":"))
#       total_seconds = hours * 3600 + minutes * 60 + seconds
#       return total_seconds
#    else:
#        return xde1

#dt = datetime.today()
#total_seconds = dt.timestamp(xde1)


xde1 = xde1.str.split('-', expand=True)[1]
xde1 = pd.to_timedelta(xde1)
xde1_hours = (86400 + xde1.dt.total_seconds()) / 3600
fig, ax = plt.subplots(figsize=(10, 4))
#xde1 = xde1 + xde2
ax.plot(xde1_hours[::10], yde1[::10], color='red', label='100 ppm Li Brine and 0.5 M NaCl')
#ax.plot(xde1[::10], yde1[::10], color='red')

ax.set_xlabel('Time (hours)')
ax.set_ylabel('Voltage (V)')
ax.legend(loc='lower left')
ax.set_title('Cyclability of a Symmetric LFP Cell in Li-rich Brine and NaCl')
ax.axvline(x=6, color='black', linestyle='--', label='Vertical Line')
ax.text(.31, .15, '24 hour pause', transform=ax.transAxes, fontsize=12)

plt.show()
