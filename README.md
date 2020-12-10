# ocr-bot
This is an telegram bot for getting ocr of a given image in which words are written in english... User can Modify this code for  working in the language support given by tesseract.

# Heroku tips.

1. User must add a key value pair. <br>
    tg_token = your telegram bot token
    
2. Add some buildpacks to install tesseract and make heroku work with python.<br>
  heroku/python<br>
  https://github.com/heroku/heroku-buildpack-apt.git <br>
  https://github.com/chanzuckerberg/heroku-buildpack-tesseract
  # Optional
  
  https://github.com/pathwaysmedical/heroku-buildpack-tesseract <br>
  https://github.com/matteotiziano/heroku-buildpack-tesseract
