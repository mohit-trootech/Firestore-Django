from firestore.utils.firestore_config import db
from django.template.loader import render_to_string
from firestore.utils.constants import Templates, TYPE_HTML
from django.core.mail import EmailMultiAlternatives


def create_firestore_object(data):
    """
    create firestore object
    """
    data.id = data._id_autoincrement()
    db.collection(data._get_ref_table()).document(data.id).set(data._get_fields())


def get_complete_articles_data():
    """
    get complete articles data
    """
    return serialize_articles_data(db.collection("Articles").stream())


def serialize_articles_data(data):
    """
    serialize articles data
    """
    serialized_data = []
    for doc in data:
        serialized_data.append(doc.to_dict())
    return serialized_data


def send_mails(subject, sender, receiver, body, attachment):
    """
    send emails

    :param subject: str
    :param sender: str
    :param receiver: list
    :param body: str
    :param attachment:
    """
    mail = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=sender,
        to=receiver,
    )
    html_message = render_to_string(Templates.NEWSLETTER.value)
    mail.attach_alternative(html_message, TYPE_HTML)
    if attachment:
        mail.attach("image.jpeg", attachment.read())
    mail.send()


def push_email_newsletter_database(email: str):
    """
    add email in newsletter database
    :param email: str
    """
    print(email)
    # database.child(NEWSLETTER).push(email)
