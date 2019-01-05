import email
import os
import shutil
import ImageHandler
import LogWriter


class EMailHandler:
    def __init__(self, path):
        if not os.path.exists(path):
            print("Allocation of the email file in the following path: " + path + " failed.")
            exit(1)
        self.email_path = path

    def process_email(self):
        msg = email.message_from_file(open(self.email_path))
        attachments = self.extract_attachments('tmp', msg)
        image = attachments[0]  # largest file - currently assuming it's the largest photo in email
        image_attributes = ImageHandler.extract_attributes(image)
        attribs = image_attributes.copy()
        print(attribs)
        attribs["Driver"] = msg["From"]
        LogWriter.write_log(attribs)



    def extract_attachments(self, dest_folder, msg):
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
                extracted_attachments.append(full_path)
        extracted_attachments.sort(key=os.path.getsize)
        return extracted_attachments




# ih = ImageHandler('images/Img_1.jpg')
# print(ih.extract_attributes())
eh = EMailHandler('example.eml')
# eh.extract_files()
eh.process_email()

