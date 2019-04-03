import io
import csv
import json
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
from pipetools import pipe, foreach, X


def download_qr_code(url_and_data):
    browser = RoboBrowser(parser='html.parser')

    return url_and_data > pipe\
        | (lambda x: browser.open(x[0], data=x[1], method='post'))\
        | (lambda x: browser.response.content)\
        | io.BytesIO\
        | json.load\
        | X["qrcode"]\
        | (lambda x: BeautifulSoup(x, features="lxml"))\
        | X.body.find('pre').text\
        | X.split()


def hex_to_qr_matrix(hex_list):
    return hex_list > pipe\
        | foreach(X.replace("#000000", "1,"))\
        | foreach(X.replace("#FFFFFF", "0,"))\
        | foreach(X[:-1])\
        | foreach(lambda x: to_int(x))\
        | list


def save_to_csv(data, name):
    with open('downloaded/' + name + '.csv', 'w') as csv_file:
        line = csv.writer(csv_file, delimiter=',')
        list(map(lambda x: line.writerow(x), data))

    csv_file.close()


def to_int(row):
    return row > pipe\
        | X.split(",")\
        | foreach(lambda x: int(x))\
        | list


def get_pattern(placement, version, data, url):
    print("Processing pattern_" + placement + "_" + str(version))
    data.update({'version': version, 'm_' + placement + '_dark': '000000'})

    (url, data) > pipe\
        | download_qr_code\
        | hex_to_qr_matrix\
        | (lambda x: save_to_csv(x, "pattern_" + placement + "_" + str(version)))

    data.update({'m_' + placement + '_dark': 'FFFFFF'})
