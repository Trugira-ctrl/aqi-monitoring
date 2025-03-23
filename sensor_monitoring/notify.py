import os
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(sensor_list):
    email = os.getenv('NOTIFICATION_EMAIL')
    print(f"Email alert to {email}: Sensors {sensor_list} are offline.")


