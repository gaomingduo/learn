import json

def response(flow):
    if "getLuckyHistory" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['lucky_history'][0]['created_at'] = "2021-03-25 22:11:00"
        data['data']['lucky_history'][0]['lucky'] = -500

        flow.response.text = json.dumps(data)