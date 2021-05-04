from mitmproxy import http


def request(flow:http.HTTPFlow)->None:
    if "getLuckyHistory" in flow.request.pretty_url:
        with open ("/Users/gaomingduo/Documents/Project/mitmproxy/boxonline.json", encoding="utf-8" ) as f:
            flow.response = http.HTTPResponse.make(
                200, #(optional) status code
                f.read(), #(optional) content
                {"Content-Type": "application/josn"}
            )