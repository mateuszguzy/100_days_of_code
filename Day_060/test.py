import os

FROM_MAIL = os.environ.get("TEST_MAIL_100_DAYS")
PASSWORD = os.environ.get("TEST_MAIL_100_DAYS_PASSWORD")

print(FROM_MAIL, PASSWORD)