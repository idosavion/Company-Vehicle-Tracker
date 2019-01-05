import email
import os
import shutil
import ImageHandler
import LogWriter

TEMP_FOLDER_PATH = "tmp"


def process_email(email_path):
    """
    check if the file exists and continue as needed
    :param email_path:
    :return:
    """
    if not os.path.exists(email_path):
        print("eml file couldn't be found. Please check the provided path.")
        exit(1)
    else:
        process_eml_file(email_path)
        print("Email was successfully parsed, data was written to log file.")


def process_eml_file(email_path):
    """
    extract the images from mail into tmp folder, extracting the data from largest photo, write to log and remove all
    the files created in the process
    :param email_path: path to eml file
    """
    msg = email.message_from_file(open(email_path))
    attachments = _extract_attachments(TEMP_FOLDER_PATH, msg)
    image = attachments[0]  # largest file - currently assuming it's the largest photo in email
    extracted_data = ImageHandler.extract_attributes(image)
    extracted_data["Driver"] = msg["From"]
    LogWriter.write_log(extracted_data)
    shutil.rmtree(TEMP_FOLDER_PATH)


def _extract_attachments(dest_folder, msg):
    """
    go through the files in files, extract them if they are in .jpeg or .jpg format
    :param dest_folder: to extract the files into
    :param msg: email message
    :return: list of all image files extracted from the email
    """
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    os.mkdir(dest_folder)
    extracted_attachments = []
    for attachment in msg.get_payload():
        attachment_type = attachment.get_content_type()
        if attachment_type in ["image/jpeg", "image/jpg"]:
            filename = attachment.get_filename()
            full_path = os.path.join(dest_folder, filename)
            open(full_path, "wb").write(attachment.get_payload(decode=True))
            extracted_attachments.append(full_path)
    extracted_attachments.sort(key=os.path.getsize)
    return extracted_attachments


