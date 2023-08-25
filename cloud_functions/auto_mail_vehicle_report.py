import sqlalchemy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from datetime import date
import io
import os
from google.cloud.sql.connector import Connector, IPTypes
import pg8000


def connect_to_database() -> sqlalchemy.engine.base.Engine:

    instance_connection_name = "total-glider-396411:us-central1:dsmpl-prod"
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user="postgres",
            password="0.AH]AeB2[C+V*[A",
            db="milkmil",
            ip_type=IPTypes.PUBLIC,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    return pool

def fetch_data_from_database(conn, d):
    query = "SELECT date, type, driver_name, reason, num_passengers, out_time, in_time, out_kms FROM milkmil_vehicle where date='{}';".format(d)
    return conn.execute(query)

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(attachment)

    server = smtplib.SMTP('smtp.office365.com', '587')
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

def main(request):
    today = date.today()
    db_connection = connect_to_database()
    fetched_data = fetch_data_from_database(db_connection, today)
    column_names = ['Date', 'Type', 'Driver Name', 'Reason', 'Passengers', 'Out Time', 'In Time', 'Out Kms']
    df = pd.DataFrame(fetched_data.fetchall(), columns=column_names)
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False)

    sender_email = "dsmpltn@outlook.com"
    sender_password = "dsmplTamilnadu"
    recipient_email = "pratishbajpai7@gmail.com"
    subject = "Vehicle Report - {}".format(today)
    body = "Please find the attached data."
    attachment = MIMEApplication(excel_buffer.getvalue())
    attachment['Content-Disposition'] = 'attachment; filename=Vehicle_{}.xlsx'.format(today)

    send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment)

    return "Success"
