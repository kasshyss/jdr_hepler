#!/usr/bin/env python

# Python import
from flask import Flask, render_template, request
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# Apps import
import m_pnj as pnj
import m_conf as conf

# Init Flask context
app = Flask(__name__, template_folder='template')
# Other inits
language = conf.get_conf('appli_context.conf')['language']
app_n =  conf.get_conf('appli_context.conf')['app_name']

# Index page html
@app.route('/')
@app.route('/index/')
@app.route('/index')
def index():
    page_conf =conf.get_conf('context_index_'+ language +'.conf')
    return render_template(
            'index.html'
            ,app_name = app_n
            ,title = page_conf['title']
            # ,subtitle = page_conf['subtitle']
            ,options = page_conf['buttons'].split(',')
            )
