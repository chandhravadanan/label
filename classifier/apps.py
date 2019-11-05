from django.apps import AppConfig
from . import slackutil

class ClassifierConfig(AppConfig):
    name = 'classifier'

    def ready(self):
        try:
            from .models import Images
            image = Images.objects.filter(label='')[:1]
            imageurl = image[0].url
            imageid = image[0].imageid
            slackutil.post_unalabeld_image_to_slack(imageurl, imageid)
        except Exception as exc:
            print('posting image to slack when app starts', exc)
        

