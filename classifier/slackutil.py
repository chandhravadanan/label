
import requests

channel_webhook_url = "https://hooks.slack.com/services/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"

slack_message_format = """{
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Image",
                    "emoji": true
                },
                "image_url": "$url",
                "alt_text": "Image"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "daisy",
                            "emoji": true
                        },
                        "value": "$imageid"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "dandelion",
                            "emoji": true
                        },
                        "value": "$imageid"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "rose",
                            "emoji": true
                        },
                        "value": "$imageid"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "sunflower",
                            "emoji": true
                        },
                        "value": "$imageid"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "tulip",
                            "emoji": true
                        },
                        "value": "$imageid"
                    }
                ]
            }
        ]
    }"""

def post_unalabeld_image_to_slack(imageurl, imageid):
    try:
        payload = slack_message_format.replace('$url', imageurl)
        payload = payload.replace('$imageid', str(imageid))
        r = requests.post(channel_webhook_url, data=payload)
        print('slack status', r.text)
    except Exception as exc:
        print('Exception occurred while posting in slack', exc)


def send_slack_response(response_url, response_msg):
    try:
        payload = "{'text':'"+ response_msg +"'}"
        r = requests.post(channel_webhook_url, data=payload)
        print('repponse status', r.text)
    except Exception as exc:
        print('Exception occurred while posting response in slack', exc)