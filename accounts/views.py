from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view
from django.core import exceptions, validators
from rest_framework.response import Response
import smtplib
import requests
import json
import os
import os.path
import base64
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps
from datetime import datetime
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Create your views here.
@api_view(['GET', 'POST'])
def analyse(request):
                
              if request.method== 'POST':
                     text = request.POST['text']
                     sia = SentimentIntensityAnalyzer()
                     score = sia.polarity_scores(text)
                     if score['compound'] >= 0.05:
                          return Response({"output":"Happy"})
                     elif score['compound'] <= -0.05:
                          if score['neg'] > score['pos']:
                               return Response({"output":"Sad"})
                          elif score['neg'] < score['pos']:
                               return Response({"output":"Angry"})
                          else:
                               return Response({"output":"Fear"})
                     else:
                        return Response({"output":"Neutral"})
              else:
                return render(request,'analyse.html')
   # [(0 is Happy), (1 is Angry), (2 is Sad), (3 is Fear)]


                      
                
    
    
 





    
