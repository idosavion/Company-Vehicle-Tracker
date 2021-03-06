import argparse
import EMailHandler
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process EML file for car fleet management")
    parser.add_argument("eml_file",help=".eml file to process")
    # parser.add_argument("eml_file",type=str, help="file to process")
    args = parser.parse_args()
    eml_path = re.sub('[\"\']', '', args.eml_file)  # remove quotes from string if found
    if eml_path[0] == "/":
        eml_path = eml_path[1:]
    email_handler = EMailHandler.process_email(eml_path)
    pass
