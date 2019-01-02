import argparse
import EMailHandler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process EML file for car fleet management")
    parser.add_argument("eml_file")
    # parser.add_argument("eml_file",type=str, help="file to process")
    args = parser.parse_args()
    eml_path = args.eml_file
    email_handler = EMailHandler.EMailHandler(eml_path)
    pass
