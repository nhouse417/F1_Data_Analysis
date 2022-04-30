import fastf1 as ff1
from fastf1 import plotting

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

#===================================

# Set up plotting
plotting.setup_mpl()

# Enable the cache for faster processing of data
# optional but definitely recommend
ff1.Cache.enable_cache('/path/to/empty/folder')

#===================================

# load session data , Imola 2022
race = ff1.get_session(2022, 'Imola', 'R')

# load lap data
race.load(laps=True, telemetry=True)

# get laps from Leclerc and Verstappen
ver_laps = race.laps.pick_driver('VER')
lec_laps = race.laps.pick_driver('LEC')

# get fastest laps from both drivers
ver_fastest_laps = ver_laps.pick_fastest()
lec_fastest_laps = lec_laps.pick_fastest()

# get telemtry from both drivers fastest laps
# get speed, throttle, brakes
# get distance for x-axis of graph
ver_telemetry = ver_fastest_laps.get_car_data().add_distance()
lec_telemetry = lec_fastest_laps.get_car_data().add_distance()

#===================================

# define subplots and set title
# 3 subplots: speed, throttle, brake
fig, ax = plt.subplots(3)
fig.suptitle("Fastest Race Lap Telemetry Comparison")

ax[0].plot(ver_telemetry['Distance'], ver_telemetry['Speed'], label='VER')
ax[0].plot(lec_telemetry['Distance'], lec_telemetry['Speed'], label='LEC')
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right", bbox_to_anchor=(0.00, 1.00))

ax[1].plot(ver_telemetry['Distance'], ver_telemetry['Throttle'], label='VER')
ax[1].plot(lec_telemetry['Distance'], lec_telemetry['Throttle'], label='LEC')
ax[1].set(ylabel='Throttle')

ax[2].plot(ver_telemetry['Distance'], ver_telemetry['Brake'], label='VER')
ax[2].plot(lec_telemetry['Distance'], lec_telemetry['Brake'], label='LEC')
ax[2].set(ylabel='Brakes')

# Hide x labels and tick labels for top plots and y ticks for right plots
for a in ax.flat:
    a.label_outer()
    
plt.show()






