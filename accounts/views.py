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
                     # create SentimentIntensityAnalyzer object
                     sia = SentimentIntensityAnalyzer()
                     # get sentiment score
                     score = sia.polarity_scores(text)
                     # get the compound score, which represents the overall emotion
                     compound_score = score['compound']
                     if compound_score >= 0.5:
                         return Response({"output":"Positive Emotion"})
                     elif compound_score > -0.5 and compound_score < 0.5:
                         return Response({"output":"Neutral Emotion"})
                     else:
                         return Response({"output":"Negative Emotion"})
              else:
                return render(request,'analyse.html')
   # [(0 is Happy), (1 is Angry), (2 is Sad), (3 is Fear)]


                      
                
    
    
 





    
