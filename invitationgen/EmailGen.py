import string
from invitationgen import MetaBundle

def build_main_instruction_location(group: string):
    return "https://www.cs.mcgill.ca/~mschie3/" + group + "/restify-study/"


def build_mirror_instruction_location(group: string):
    return "https://kartoffelquadrat.eu/mirror/" + group + "/restify-study/"


def generate_email_content(meta: MetaBundle):
    # Modify the template string to match this participant
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AI am happy to inform you that your application to participate in the RESTify experiment has been accepted!%0D%0A%0D%0ADetailed instructions await you here: MAIN_COLOUR_SERVER_LOCATION %0D%0AIf above link is slow due to server load, you may also use this mirror: MIRROR_COLOUR_SERVER_LOCATION%0D%0A * Please note that the links are personal and should not be shared or altered.%0D%0A * The deadline for all your file uploads is: Sunday, July 24th 2022%0D%0A%0D%0APlease read all instructions very carefully and especially respect the presented task order, since otherwise your data and efforts may be unusable for our research.%0D%0A * Throughout your tasks you will be asked for a personal pseudonym. It is: %22PSEUDONYM%22 %0D%0A(Please do not share your pseudonym, so we can ensure your anonymity)%0D%0A * At the end of the experiment I will ask you to upload certain files to this personal upload location: ONEDRIVE_UPLOAD_LOCATION %0D%0A(Please do not share this link either)%0D%0A%0D%0ADo not hesitate to contact me in case of technical problems during the phase named %22Preliminaries%22 (that is the setup phase before your actual tasks, where we prepare your system)%0D%0A%0D%0AThanks again for your interest, I wish you good luck and lots of fun with the experiment!%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    generic_email_html_button = generic_email_html_button.replace("MAIN_COLOUR_SERVER_LOCATION", build_main_instruction_location(meta.get_group_name()))
    generic_email_html_button = generic_email_html_button.replace("MIRROR_COLOUR_SERVER_LOCATION",
                                      build_mirror_instruction_location(meta.get_group_name()))
    generic_email_html_button = generic_email_html_button.replace("PSEUDONYM", meta.get_pseudonym())
    generic_email_html_button = generic_email_html_button.replace("ONEDRIVE_UPLOAD_LOCATION", meta.get_upload_location())
    return generic_email_html_button

def generate_reminder_content(meta: MetaBundle):
    # Modify the template string to match this participant
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment DEADLINE Approaching&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AThis is a reminder that you are enroled in the RESTify study and have not yet uploaded the requested files.%0D%0ADeadline for all file uploads is: Sunday, July 24th 2022%0D%0A%0D%0AIt is highly recommended to commence the study as early as possible, since you may encounter technical diffculties that need our assistance.%0D%0A(In case you already uploaded, yet still received this email, please let me know. I will verify you submission as soon as I can!)%0D%0A%0D%0A%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    return generic_email_html_button


def generate_extension_content(meta: MetaBundle):
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment Confirmation Needed&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AYou are receiving this email because you registered for the RESTify study, but did not provide the requested study data until the provided deadline, which was Sunday evening.%0D%0A%0D%0AYour participation in the study is valuable to us, therefore we offer you an extended deadline: Sunday, July 31st 2022 23PM59.%0D%0A%0D%0AIf you still intend to participate, please let us know: Either by submitting before Wednesday noon or by sending us an email before Wednesday noon where you confirm your active commitment to the study.%0D%0A%0D%0AIf we have not heard back until Wednesday noon we unfortunately have to pass your spot to a participant on the waiting list and you will no longer be able to participate.%0D%0A%0D%0ABest, and hoping to hear from you soon,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    return generic_email_html_button

def generate_kicked_content(meta: MetaBundle):
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment Removal Notice&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AThis is to notify you that you have been removed from participation in the RESTify study due to inactivity. You can no longer upload files or request compensation.%0D%0A%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    return generic_email_html_button


def generate_sorry_content(meta: MetaBundle):
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment Compensation&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AWe have received and evaluated your submission and it is complete.%0D%0AUnfortunately we currently experience severe issues with the distribution of Amazon vouchers. We have ordered all at once and Amazon considered it a fraud attempt. I am very sorry for the delay an inconvenience. We are working hard on fixing the situation on our side. I personally take care that you will receive the compensation as soon as possible. Thank you for your understanding, and again thank you very much for your participation.%0D%0A%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    return generic_email_html_button

def generate_code_content(meta: MetaBundle):
    generic_email_html_button = '<a href="mailto:PARTICIPANT_EMAIL?bcc=maximilian.schiedermeier@mcgill.ca&subject=RESTify Experiment Amazon Code&amp;body=Hello FIRST_NAME,%0D%0A%0D%0AHere is your amazon gift card code.%0D%0A%0D%0ACODEHERE%0D%0A%0D%0APlease immediately sign the attached form and send it back, so I can claim it back from the university.%0D%0A%0D%0ABest,%0D%0AMaximilian Schiedermeier" style="text-decoration: none">📧</a>'
    generic_email_html_button = generic_email_html_button.replace("PARTICIPANT_EMAIL", meta.get_email())
    generic_email_html_button = generic_email_html_button.replace("FIRST_NAME", meta.get_first_name())
    return generic_email_html_button