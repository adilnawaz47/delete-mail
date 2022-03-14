import imaplib

my_email = "######2@gmail.com"
app_generated_password = "##########"

#initialize IMAP object for Gmail
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#login to gmail with credentials
imap.login(my_email, app_generated_password)

imap.select("INBOX")

status, messages = imap.search(None, "ALL")
#,
#convert the string ids to list of email ids
messages = messages[0].split(b' ')
print("Deleting mails")
count =1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1
print("All selected mails have been deleted")

# delete all the selected messages 
imap.expunge()
# close the mailbox
imap.close()

# logout from the account
imap.logout()