import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL=os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generation_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is misssing.")

promt=f"""
you are a professional gmail email writing assistant.

covert the user's voice command into a professional email.

Rules:
-Do not copy the command literally.
-Do not explain anything .
-Do not invert names ,dates, prices, companies , attachment, or facts.
-Keep the email natural and concies.

Output exactly:

SUBJECT:<subject>


