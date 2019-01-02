from email import message_from_file
import os

from eml_parser import eml_parser


class EMailHandler:
    def __init__(self, path):
        if not os.path.exists(path):
            print("Allocation of the email file in the following path: " + path + " failed.")
            exit(1)
        self.path = path
        self.content = EMailHandler.parseFile(path)


    @staticmethod
    def parseFile(path):
        with open(path,'rb') as emlf:
            raw_email = emlf.read()
        parsed_eml = eml_parser.decode_email_b(raw_email)
        return parsed_eml


