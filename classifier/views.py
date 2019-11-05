from django.shortcuts import render
from django.http import HttpResponse
from classifier.models import Images
from . import slackutil
import json

# Create your views here.

labels = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def slack_incoming_action(request):
    try:
        payload_str = request.POST.get('payload')
        payload_obj = json.loads(payload_str)
        action = payload_obj.get('actions')[0]
        imageid = action.get('value')
        button = action.get('text')
        label = button.get('text')
        check_and_update_label(int(imageid), label)
        response_url = action.get('response_url')
        response_message = 'image labeled as '+ label
        slackutil.send_slack_response(response_url, response_message)
        post_next_unlabeled_image()
        return HttpResponse('Ok')
    except Exception as exc:
        print('Exception occurred in slack post', exc)
        return HttpResponse(status=500)
        
        
def check_and_update_label(imageid, label):
    if imageid <= 0:
        raise Exception("INVALID_IMAGE_ID")

    if label not in labels:
        raise Exception("INVALID_LABEL")

    image = Images.objects.get(imageid=imageid)
    image.label = label
    image.save()


def post_next_unlabeled_image():
    try:
        image = Images.objects.filter(label='')[:1]
        imageurl = image[0].url
        imageid = image[0].imageid
        slackutil.post_unalabeld_image_to_slack(imageurl, imageid)
    except Exception as exc:
        print('Exception while posting image to slack', exc)