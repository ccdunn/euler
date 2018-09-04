from subprocess import call
import os
import re
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.axes as axs


prefix_lookup = {
    's': 1,
    'ms': 1e-3,
    'us': 1e-6
}


def time2sec(txt):
    txts = txt.split()
    return float(txts[0])*prefix_lookup[txts[1]]

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(os.path.join(dir_path, ".."))
log_fn = os.path.join(dir_path, "log_verify.txt")
f = open(log_fn, "w")
call(["euler", "--verify-all"], stdout=f)

f = open(log_fn, "r")
txt = f.read()
times = re.findall(r'Time elapsed: user: ([^,]+)\D+([^,]+)\D+([^\n]+)', txt)
part_pattern = '---------------------------------------------------------------\nC = correct, I = incorrect, E = error, S = skipped, . = missing\n\n'
passes = re.findall(r'[CIES\.]+', txt.partition(part_pattern)[-1])

user_times_pass = np.nan*np.ones((len(times), ))
user_times_fail = np.zeros((len(times), ))
for n in range(len(times)):
    if passes[n] == 'C':
        user_times_pass[n] = time2sec(times[n][0])
    else:
        user_times_fail[n] = 1

user_times_fail *= np.nanmin(user_times_pass[np.where(user_times_pass)[0]])/2
plt.plot(range(1, len(times)+1), user_times_pass, 'o')
ax = plt.gca()
ax.axhline(y=np.nanmean(user_times_pass), c=[0.9, 0.9, 0.9])
plt.yscale("log")
plt.xlabel("Euler Problem")
plt.ylabel("Execution Time (s)")
plt.savefig(os.path.join(dir_path, "times.png"), bbox_inches='tight')


