import os
import time
import requests
from gooddata_sdk import GoodDataSdk

host = os.getenv("GOODDATA_HOST")
token = os.getenv("GOODDATA_TOKEN")
sdk = GoodDataSdk.create(host, token)
workspace_id = os.getenv("GOODDATA_WORKSPACE_ID")
visualization_id = os.getenv("GOODDATA_VISUALIZATION_ID")
dashboard_id = os.getenv("GOODDATA_DASHBOARD_ID")

request_visual = requests.post(
    f"{host}/api/v1/actions/workspaces/{workspace_id}/export/visual",
    json={
        "dashboardId": f"{dashboard_id}",
        "fileName": "export-demo-dashboard"
    },
    headers={
        "Authorization": f"Bearer {token}",
        "Content-type": "application/json"
    }
)

export_id = request_visual.json()["exportResult"]

request_visual = requests.get(
    f"{host}/api/v1/actions/workspaces/{workspace_id}/export/visual/{export_id}",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-type": "application/pdf"
    }
)

status = True

while status:
    if (request_visual.status_code != 200):
        request_visual = requests.get(
            f"{host}/api/v1/actions/workspaces/{workspace_id}/export/visual/{export_id}",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-type": "application/json"
            }
        )
        time.sleep(5)
    else:
        print("status code is 200")
        status = False

with open('./src/dashboard.pdf', 'wb') as f:
    f.write(request_visual.content)
