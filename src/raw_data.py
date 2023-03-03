import os
from gooddata_pandas import GoodPandas

from send_email import send_email


host = os.getenv("GOODDATA_HOST")
token = os.getenv("GOODDATA_TOKEN")
gp = GoodPandas(host, token)
workspace_id = os.getenv("GOODDATA_WORKSPACE_ID")
visualization_id = os.getenv("GOODDATA_VISUALIZATION_ID")
frames = gp.data_frames(workspace_id)
subject = "Scheduled report from GoodData"
body = "Digest from GoodData"
sender = "patrik.braborec@gooddata.com"
recipients = ["patrikbraborec@gmail.com"]
password = os.getenv("EMAIL_PASSWORD")


def store_visualization_data(visualization_id):
    visualization_frame = frames.for_insight(visualization_id)
    visualization_frame.to_csv("./src/visualization.csv")


store_visualization_data(visualization_id)
send_email(subject, body, sender, recipients, password)
