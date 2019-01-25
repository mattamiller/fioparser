
import os
import json

fio_results_dir = '/Users/matthew.miller/Desktop/fio/intel_ssd/'
scrapper_output = 'output/'
output = open("summary_intelssd.txt", "w+")
device_name = "Sample Intel SSD"

for filename in os.listdir(fio_results_dir):
    if filename.endswith("fio.json"):
        f = open(fio_results_dir+filename)
        rjson = f.read()
        rdata = json.loads(rjson)

        test_name = filename
        ninetieth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['95.000000'])*.000001)
        ninetieninth_percentile = str((rdata['jobs'][0]['read']['clat_ns']['percentile']['99.000000'])*.000001)
        bw_mean = str((rdata['jobs'][0]['read']['bw_mean'])*.0001)

        output.write("" + device_name+"," )
        output.write("" + test_name+",")
        output.write("" + ninetieth_percentile +",")
        output.write("" + ninetieninth_percentile+",")
        output.write("" + bw_mean+"\n")

output.close()