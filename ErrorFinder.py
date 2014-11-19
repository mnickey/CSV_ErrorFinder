import csv
import argparse
import logging, sys
from pprint import pprint as pp
from pprint import pformat as pf
import sys
#---------------
""" Create a logging file for debugging """
logging.basicConfig(filename="output.log", level=logging.DEBUG)
#---------------
""" Create the parser """
def make_parser():
    logging.info("Create parser")
    description = "Command line tool for csv error retreival"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filename', type=argparse.FileType('rt'), nargs=1)
    return parser
#---------------
def csv_dict_reader(file_obj):
    """ Read a CSV file using csv.DictReader """
    multiple_count = 0
    id_not_specified_count = 0
    unfound_account = 0
    invalid_email_count = 0
    data_value_too_large = 0
    unknown_errors_found = 0
    state_code = 0

    reader = csv.DictReader(file_obj, delimiter=',')
    writer = csv.writer(file_obj, delimiter=',')

    for line in reader:
        if "multiple" in line["ERRORS"]:
            multiple_count += 1
        elif "Id not specified in an update call" in line["ERRORS"]:
            id_not_specified_count += 1
        elif "Could not find Account" in line["ERRORS"]:
            unfound_account += 1
        elif "invalid email address" in line ["ERRORS"]:
            invalid_email_count += 1
        elif "data value too large" in line ["ERRORS"]:
            data_value_too_large += 1
        elif "A valid two-letter US State Code" in line["ERRORS"]:
            state_code += 1
        else:
            unknown_errors_found += 1

    print "Error Count Total: {}".format(multiple_count + id_not_specified_count + unfound_account + invalid_email_count + data_value_too_large + state_code + unknown_errors_found)
    print "\tMultiple Accounts Count: {0}\n\tUnspecified ID: {1}\n\tUnfound Account: {2}\n\tInvalid Email: {3}\n\tData Value Too Large: {4}\n\tState Codes: {5}\n\t---------- \n\tUnknown Errors Found: {6}".format(
        multiple_count, id_not_specified_count, unfound_account, invalid_email_count, data_value_too_large, state_code, unknown_errors_found )
    return
#---------------
def main():
    parser = make_parser()
    args = parser.parse_args()
    # args = vars(args)
    path = "output.csv"
    with open(args["filename"]) as f_obj:
        csv_dict_reader(f_obj)
    return
#---------------
if __name__ == '__main__':
    main()
