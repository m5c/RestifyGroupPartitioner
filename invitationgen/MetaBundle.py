# Meta information about a participant only required for sending the "hired" email
import string


def extract_first_name(name):
    return name.split('-')[0].capitalize()


class MetaBundle:

    def __init__(self, name, email):
        self.first_name = extract_first_name(name)
        self.email = email
        self.pseudonym = ""
        self.upload_location = ""
        self.group_name = ""

    def get_first_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def get_pseudonym(self):
        return self.get_pseudonym

    def get_upload_location(self):
        return self.upload_location

    def get_group(self):
        return self.group

    def set_pseudonym(self, pseudonym: string):
        self.pseudonym = pseudonym

    def set_upload_location(self, upload_location: string):
        self.upload_location = upload_location

    def set_group_name(self, group_name: string):
        self.group_name = group_name
