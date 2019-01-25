

import os
import json
import re

# set variables
results_dir = '/Users/matthew.miller/Desktop/fio/'
comparisons_dir = '/Users/matthew.miller/Desktop/comparisons/'
dir_contents = os.listdir(results_dir)

for device in dir_contents:
    if re.match("^[a-zA-Z]+.*", device):
        test_list = results_dir+device
        count = 0
        while count < len(os.listdir(test_list)):
            filename = os.listdir(test_list)[count]
            full_path = results_dir + device + "/" + filename
            # print(full_path)

            if full_path.endswith("fio.json"):
                f = open(results_dir + device + "/" + filename)
                rjson = f.read()
                rdata = json.loads(rjson)

                ninetyfifth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['95.000000']) * .000001)
                ninetyninth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['99.000000']) * .000001)
                bw_mean = str((rdata['jobs'][0]['read']['bw_mean']) * .0001)

                output = open(comparisons_dir + filename, "a")
                output.write(device+","
                             +ninetyfifth_percentile+","
                             +ninetyninth_percentile+","
                             +bw_mean+"\n"
                             )
                output.close()
            count = count + 1


