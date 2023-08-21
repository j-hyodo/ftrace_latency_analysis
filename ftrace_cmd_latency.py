import argparse

parser = argparse.ArgumentParser(description="ftrace command latency", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file",help="fTrace log file")
args = parser.parse_args()


