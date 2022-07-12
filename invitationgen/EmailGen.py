import string
from invitationgen import MetaBundle


def build_main_instruction_location(group: string):
    return "https://www.cs.mcgill.ca/~mschie3/" + group + "/restify-study/"


def build_mirror_instruction_location(group: string):
    return "https://kartoffelquadrat.eu/mirror/" + group + "/restify-study/"


def generate_email_content(meta: MetaBundle):
    # Modify the template string to match this participant
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AI am happy to inform you that your application to participate in the RESTify experiment has been accepted!%0D%0A%0D%0ADetailed instructions await you here: MAIN_COLOUR_SERVER_LOCATION %0D%0A(If above link is slow due to server load, you may also use this mirror: MIRROR_COLOUR_SERVER_LOCATION )%0D%0A * Please note that the links are personal and should not be shared or altered.%0D%0A * The deadline for all your file uploads is: Sunday, July 24th 2022%0D%0A%0D%0APlease read all instructions very carefully and especially respect the presented task order, since otherwise your data and efforts may be unusable for our research.%0D%0A * Throughout your tasks you will be asked for a personal pseudonym. It is: PSEUDONYM %0D%0A(Please do not share your pseudonym, so we can ensure your anonymity)%0D%0A * At the end of the experiment I will ask you to upload certain files to this personal upload location: ONEDRIVE_UPLOAD_LOCATION %0D%0A(Please do not share this link either)%0D%0A%0D%0ADo not hesitate to contact me in case of technical problems during the Preliminaries phase (setup phase before your actual tasks)%0D%0A%0D%0AThanks again for your interest, I wish you good luck and lots of fun with the experiment!%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    generic_email_html_button.replace("MAIN_COLOUR_SERVER_LOCATION", build_main_instruction_location(meta.get_group_name()))
    generic_email_html_button.replace("MIRROR_COLOUR_SERVER_LOCATION",
                                      build_mirror_instruction_location(meta.get_group_name()))
    generic_email_html_button.replace("PSEUDONYM", meta.get_pseudonym())
    generic_email_html_button.replace("ONEDRIVE_UPLOAD_LOCATION", meta.get_upload_location())
    return generic_email_html_button
