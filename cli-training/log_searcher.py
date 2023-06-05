import argparse
import re

def search_ips(log_file):
  ips_list = set()
  with open(log_file, "rt") as current_file:
    for entry in current_file.readlines():
      #ip_address_match = re.search(r"([0-9]{1,3}\.){3}[0-9]{1,3}", entry)
      ip_address_match = re.search(r"((2[0-5][0-5]\.)|(1[0-9][0-9]\.)|([0-9]?[0-9])\.){3}((2[0-5][0-5])|(1[0-9][0-9])|([0-9]?[0-9]))", entry)
      if ip_address_match:
        ips_list.add(ip_address_match.group(0))
    print(current_file.name)
    for ip in ips_list:
      print(ip)

parser = argparse.ArgumentParser(prog="cli-training", description='Program to process your log files')
parser.add_argument('-I', '--ip_address', action='store_true')
parser.add_argument('file', help='file to be searched for data', nargs='+')

args = parser.parse_args()

for log_file in args.file:
    if args.ip_address:
      search_ips(log_file)

