
import os
import json

# set variables
fio_results_dir = '/Users/matthew.miller/Desktop/fio/intel_ssd/'
device_name = "SampleIntelSSD"
output = open(device_name+"_output.txt", "w+")

# Loop through JSON and pull out meaningful metrics
for filename in os.listdir(fio_results_dir):
    if filename.endswith("fio.json"):
        f = open(fio_results_dir+filename)
        rjson = f.read()
        rdata = json.loads(rjson)

        ninetyfifth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['95.000000'])*.000001)
        ninetyninth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['99.000000'])*.000001)
        bw_mean = str((rdata['jobs'][0]['read']['bw_mean'])*.0001)

        # Write variables to csv
        output.write("" + device_name+","
                     + filename+","
                     + ninetyfifth_percentile+","
                     + ninetyninth_percentile+","
                     + bw_mean+"\n"
                     )

output.close()