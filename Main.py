import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
def send_email(to_email, subject, message):
    gmail_user = ''
    gmail_password = ''

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        header = f'To:{to_email}\nFrom: {gmail_user}\nSubject:{subject}\n'
        message = header + message
        server.sendmail(gmail_user, to_email, message)
        print("Email sent!")
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        server.quit()

# Read the email addresses from the text file
with open("emails.txt") as f:
    email_list = f.read().splitlines()

# Compose the message
list_sub = ['Boost Your Instagram Growth Organically with Instaresso - Following all Instagram policies', 'Grow your Instagram Account Organically - Following all Instagram policies', 'One tool to grow your Instagram Organically - Following all Instagram policies', 'Save time and grow all of your Instagram accounts with ease']
email_count = 0

message2 =  """

<html>
<style>
      p {
        font-size: 13px;
      }
    </style>
  <body>
    <h3>
      <b>#Boost Your Instagram Growth with Instaresso</b>
    </h3>
    <p>
      <i>Instaresso</i> is designed to interact with users in real-time just like real human and help you grow your engagement and reach  , thus helping you grow your account organically by following all Instagram policies to reduce detection.
    </p>
    <p>
      <b>Here are some of the features that the bot offers:</b>
    </p>
    <ul>
      <li>Follow, Like, Comment by Hashtags, Location, Target post, Target user followers, Post likers, Feeds, Specific users.</li>
      <li>Unfollow functions like Unfollow everyone, Unfollow except for allow list, Unfollow users followed by the bot, Remove followers.</li>
      <li>Story functions like Story view, Story reply, Story react, Story like.</li>
      <li>Direct Message functions like DMs to Target users, post likers, specific users, DMs by hashtags, location, following, and new followers.</li>
      <li>Filters like skipping users without profile pictures, private accounts, and users with a high number of followers and following.</li>
      <li>Safety features like random feed interaction, action limit, custom delay between actions, scheduler, proxy support, and automatic verification for OTP.</li>
      <li> AND MORE! </LI>
    </ul>
    <h4>
      Please reply to this email if you have any questions or if you would like to try out the bot.<br>
    </h4>
    <h4>
      Best regards,<br>
      Creator Of Instaresso
    </h4>
  </body>
</html>
"""
part2 = MIMEText(message2, 'html')
# Loop through the email addresses and send the email
while email_count < 20100:
    for email in email_list[email_count:email_count+500]:
        subject = random.choice(list_sub)
        send_email(email, subject, str(part2))
    email_count += 500
    time.sleep(86400) 

