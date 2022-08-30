#!/usr/bin/python3
#https://stackoverflow.com/questions/13210737/get-only-new-emails-imaplib-and-python
import os, sys, time, re, asyncio, signal, random
import email, imaplib, smtplib, ssl
from email.mime.text import MIMEText
from datetime import datetime, date

os.system("clear")
print("\n")

#Main Account Credential Variables
username = "Your Email"
password = "Your Password"

#Other Email Accounts
main_email_user = "<Email Address>"
alternative_email_user = "<Email Address 2>"
alternative_email_user_2 = "<Email Address 3>"
alternative_email_user_3 = "<Email Address 4>"

#Unverified Email Reply Text
false_text_one = "Hello it seems like this email was sent to you by mistake..."
false_text_two = "This email was sent automatically. Please do not email this user again. Thank you!"
false_text_three = "Oops, this email was sent by mistake..."
false_text_four = "Email UNVERIFIED, please do not email this user again."
false_text_five = "Email username unconfirmed, this email was sent because you sent an email to this user. Do NOT send an email to this user."
false_text_six = "You have emailed this user. Please do not send another email."
false_text_seven = "Hello! You have sent an email to this user by accident."
false_text_eight = "Salutations! Did you send an email to this user by accident? Its ok..."
false_text_nine = "You've gotten this email because you sent an email to this user, please becareful next time!"
false_text_ten = "It seems like you sent an email to this user by accident."
false_bid_text = [false_text_one,false_text_two, false_text_three, false_text_four, false_text_five, false_text_six, false_text_seven, false_text_eight, false_text_nine, false_text_ten]

#Menu Variable Protocol
menu_prompt = "The following are email commands (send an email to the following to command the script): \n \t 1.) menu - to view the menu selection \n \t 2.) deadzone - stop bidding on shift until midnight \n \t 3.) shutdown - to completely shutdown script "
deadzone_prompt = "Deadzone protocol has been initiated, the script will stop bidding until midnight"
shutdown_selection_prompt = "Shutdown protcol has been initiated, the script will now shutdown..."

#Gmail Email Variables IMAP Protcol
Gmail_IMAP_server = 'imap.gmail.com'

#Gmail Email Variables SMTP Protcol
SMTP_GMAIL_server = "smtp.gmail.com"
context = ssl.create_default_context()

#Gmail Network Ports
IMAP_Gmail_Port = 993
SMTP_Gmail_Port = 587

@asyncio.coroutine
async def sending_bidding_email(email_message, email_from, subject):
    email_id_reference = email_message
    #Email Body Content Details
    for part in email_id_reference.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            find_id = body.decode('utf-8')
            digit = re.search(r'Y\d{1,}', find_id)
            b = digit.group(0)
            continue
        else:
            continue

    #Sending e-mail context logging into SMTP server
    sending_gmailahs = smtplib.SMTP(SMTP_GMAIL_server, SMTP_Gmail_Port)
    sending_gmailahs.starttls(context=context)
    sending_gmailahs.login(username, password)

    #Variable defined
    email_reply_text = b
    sending_email_to = email_from

    #Messages encoded into MIMETEXT and creating e-mail
    messages = MIMEText(email_reply_text)
    messages["From"] = username
    messages["To"] = sending_email_to
    messages["Subject"] = subject
    sending_gmailahs.sendmail(username, sending_email_to, messages.as_string())
    del subject
    del sending_email_to
    del b
    del digit
    sending_gmailahs.quit()
    return

#The decorator enables legacy generator-based coroutines to be compatible with async/await code
@asyncio.coroutine
async def unverified_email(email_message, email_from, subject):

    email_messages_unverified_user = email_message
    for part in email_messages_unverified_user.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            find_id = body.decode('utf-8')
            refid = re.search(r'Y\d{1,}', find_id)
            newdigit = refid.group(0)
            continue
        else:
            continue

    #Sending e-mail context logging into SMTP server
    sending_gmailahs = smtplib.SMTP(SMTP_GMAIL_server, SMTP_Gmail_Port)
    sending_gmailahs.starttls(context=context)
    sending_gmailahs.login(username, password)

    #Variable defined
    email_reply_text = newdigit
    sending_email_to = email_from
    random_text = random.choice(false_bid_text)

    #Messages encoded into MIMETEXT and creating e-mail
    messages = MIMEText(email_reply_text + "\n\n" + random_text)
    messages["From"] = username
    messages["To"] = sending_email_to
    messages["Subject"] = subject
    sending_gmailahs.sendmail(username, sending_email_to, messages.as_string())
    del subject
    del sending_email_to
    del random_text
    del newdigit
    del refid
    sending_gmailahs.quit()
    return

@asyncio.coroutine
async def main_email_user_recieved(email_message, email_from, subject):

    email_messages_verified_user = email_message
    for part in email_messages_verified_user.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            find_id = body.decode('utf-8')
            ref_id = re.search(r'Y\d{1,}', find_id)
            ref_digit = ref_id.group(0)
            continue
        else:
            continue

    #Sending e-mail context logging into SMTP server
    sending_gmailahs = smtplib.SMTP(SMTP_GMAIL_server, SMTP_Gmail_Port)
    sending_gmailahs.starttls(context=context)
    sending_gmailahs.login(username, password)

    #Variable defined
    email_reply_text = ref_digit
    sending_email_to = email_from

    #Messages encoded into MIMETEXT and creating e-mail
    messages = MIMEText(email_reply_text + "\n\n" + "Sincerely," + "\n\n" + "Mark Tan")
    messages["From"] = username
    messages["To"] = sending_email_to
    messages["Subject"] = subject
    sending_gmailahs.sendmail(username, sending_email_to, messages.as_string())
    del subject
    del sending_email_to
    del ref_digit
    del ref_id
    sending_gmailahs.quit()
    return

async def ahs_response_email():
    #Other Variables
    timePoint = time.time()
    z = 0
    y = 0

    #Gmail Email Variables IMAP Protocol
    mail = imaplib.IMAP4_SSL(Gmail_IMAP_server, IMAP_Gmail_Port)
    mail.login(username, password)
    latest_email_uid = ''
    email_from = ''

    #Other Variables
    loopback = True

    while loopback:

        #Loop Terminal Print label
        clock_label = "\t\t\tAUTOMATED EMAIL BIDDING SCRIPT CLOCK\n"
        decorator = "_" * 70
        line = "\t" + decorator + "\n"

        #Print Current Time and Elapsed Time
        local_time = time.localtime()
        now = datetime.now()
        wake_up = now.replace(hour=5, minute=0, second=0, microsecond=0)
        late_pickup = now.replace(hour=23, minute=59, second=0, microsecond=0)
        currentTime = time.gmtime(time.time() - timePoint)
        timeStr = time.strftime("\tElapsed Time: %H:%M:%S\n", currentTime)

        #Date and Time parsing and Terminal Display
        date_today = now.strftime("\n\tDate: %A, %B %d, %Y")
        current_time = time.strftime("\n\tCurrent Time: %I:%M:%S %p",local_time)
        the_current_email_user = "\tCurrent Email: " + username + "\n"
        email_sent_messaged = "\tEmail Messaged Recieved: {:d}\n".format(y)
        email_not_sent = "\tEmail Messaged Not Sent: {:d}\n".format(z)
        email_recieved_from = "\tLast Email Recieved From: {}\n".format(email_from)
        new_time = clock_label + line + date_today + current_time + timeStr + the_current_email_user + email_sent_messaged + email_not_sent + email_recieved_from + line + "\r"
        print(new_time, end="\r", file=sys.stdout, flush=True)
        sys.stdout.flush()
        sys.stdout.write("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F")

        #Select Mail Inbox
        mail.select(mailbox='INBOX', readonly=False)
        result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
        i = len(data[0].split())

        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')  
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)

            # Header Details
            email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
            email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
            subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
            emailaddresssearch = re.search(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', email_from)
            check_email = emailaddresssearch.group(0)
            checked_email = check_email.lower()

            #Check who the email is from
            if checked_email == ahs_staffing:
                if (now >= wake_up) and (now <= late_pickup):
                    await asyncio.create_task(sending_bidding_email(email_message, email_from, subject))
                    del email_to
                    y = y + 1
                else:
                    z = z + 1

            elif checked_email == main_email_user:
                if (now >= wake_up) and (now <= late_pickup):
                    await asyncio.create_task(main_email_user_recieved(email_message, email_from, subject))
                    del email_to
                    y = y + 1
                else:
                    z = z + 1

            else:
                await asyncio.create_task(unverified_email(email_message, email_from, subject))
                y = y + 1

            del emailaddresssearch
            del check_email
            del checked_email

def shutdown_input(sig, frame):
    os.system('clear')
    print("\n\n\t Automated e-mail bidding script is now exiting.... \n\n\n")
    sys.exit(0)

async def main():
    while True:
        await ahs_response_email()
        await asyncio.sleep(1)

signal.signal(signal.SIGINT, shutdown_input)
asyncio.run(main())
