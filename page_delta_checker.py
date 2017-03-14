# Import requests so we can use HTML
import requests

# Import Time so we can use a delay
import time

# Import smtplib so we can send emails
import smtplib

# Import MIMEText, which we will use to create the message
from email.mime.text import MIMEText


# while this is true (it is true by default),
def main():
    starting_occurrences = 0
    starting_size = 0

    while True:
        # set the url
        url = "PLACEHOLDER"

        # set the headers like we are a browser,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        # download the page
        response = requests.get(url, headers=headers)
        content = response.content
        content_size = len(response.content)
        num_occurrences = content.count("PLACEHOLDER")

        cont = False

        # see if anything has changed
        if num_occurrences != starting_occurrences or content_size != starting_size:
            # create an email message with just a subject line,
            msg = MIMEText("Previous Size: %d New Size: %d Previous Num Occurrences: %d New Num Occurrences: %d" % 
                           (starting_size, content_size, starting_occurrences, num_occurrences))
            me = "PLACEHOLDER"
            you = "PLACEHOLDER"
            msg['Subject'] = "PLACEHOLDER"
            # set the 'from' address,
            msg['From'] = "PLACEHOLDER"
            # set the 'to' addresses,
            msg['To'] = "PLACEHOLDER"

            # setup the email server,
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password
            server.login("PLACEHOLDER", "PLACEHOLDER")

            # send the email
            server.sendmail(me, [you], msg.as_string())
            # disconnect from the server
            server.quit()

            time.sleep(5)
            starting_occurrences = num_occurrences
            starting_size = content_size

        else:
            # wait 60 seconds,
            time.sleep(60)


if __name__ == "__main__":
    main()
