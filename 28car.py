#!/usr/bin/env python
# -*- coding: utf-8 -*-

from envelopes import Envelope, GMailSMTP
from tendo import singleton
from bs4 import BeautifulSoup
import requests

me = singleton.SingleInstance()

s = requests.Session()

r1 = s.post('http://dj1jklak2e.28car.com/sell_ico.php', data={'h_srh': 'swift', 'h_srh_ty': 1, 'h_f_tr': 2})
soup = BeautifulSoup(r1.text, 'lxml')

rw_0 = soup.body.findAll('td', {'id': 'rw_0'})[0].contents[0]
print rw_0
