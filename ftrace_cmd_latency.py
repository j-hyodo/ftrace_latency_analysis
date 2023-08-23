import argparse

parser = argparse.ArgumentParser(description="ftrace command latency", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file",help="fTrace log file")
args = parser.parse_args()
config = vars (args)
print (config)

f = open("nvme-trace1.log", "r")
fw = open("ftrace_formatted.log", "w")

while True:
    line = f.readline()
    if not line:
        break
    indx = line.find(': nvme')
    if indx != -1:
        fw.write(line[indx-13:].replace(":",","))

fw.close()
f.close()

f = open("ftrace_formatted.log", "r")
fw = open("ftrace_write_parsed.csv", "w")

setup_patt='nvme_cmd_write' 
#nvme_cmd_read, nvme_cmd_dsm

lines = f.readlines()
for i in range (0, len(lines)):
    line = lines[i]
    index = line.find(setup_patt)
    if indx == -1:
        continue
    else:
        indx_qid = line.find('qid')
        indx_nsid = line.find('nsid')
        comp_str_patt = line[indx_qid:indx_nsid-1]
 #       print (lines[i])
        fw.write (lines[i])


        for j in range(i+1, len(lines)):
            index = lines[j].find(comp_str_patt)
            if indx == -1:
                 continue
            else:
#                print (lines[j])
                fw.write(lines[j])
                break;

fw.close()
f.close()