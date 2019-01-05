import email
import os
import shutil

import ImageScraper


class EMailHandler:
    def __init__(self, path):
        if not os.path.exists(path):
            print("Allocation of the email file in the following path: " + path + " failed.")
            exit(1)
        self.email_path = path

    def process_email(self):
        attachments = self.extract_files()
        image = attachments[0]  # largest file
        image_handler = ImageScraper.ImageHandler(image)
        image_attributes = image_handler.extract_attributes()
        print(image_attributes)

    def extract_files(self, dest_folder='tmp'):
        msg = email.message_from_file(open(self.email_path))
        if os.path.exists(dest_folder):
            shutil.rmtree(dest_folder)
        os.mkdir(dest_folder)
        extracted_attachments = []
        for attachment in msg.get_payload():
            ctype = attachment.get_content_type()
            if ctype in ['image/jpeg', 'image/jpg']:
                filename = attachment.get_filename()
                full_path = os.path.join(dest_folder, filename)
                open(full_path, 'wb').write(attachment.get_payload(decode=True))
                extracted_attachments.append(filename)
        extracted_attachments.sort(key=os.path.getsize)
        return extracted_attachments

    def get_sender(self):
        msg = email.message_from_file(open(self.email_path))
        pass



# ih = ImageHandler('images/Img_1.jpg')
# print(ih.extract_attributes())
eh = EMailHandler('original_msg.txt')
# eh.extract_files()
eh.process_email()
eh.get_sender()
