#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   liuyuqi
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2020/06/01 17:46:12
@Version :   1.0
@License :   Copyright © 2017-2020 liuyuqi. All Rights Reserved.
@Desc    :   每日获取最新 host.deny
'''

import requests
import os
import sys
import re
import time
import json
import user_agent

url = "http://antivirus.neu.edu.cn/ssh/lists/neu_sshbl_hosts.deny"
resultFile = r'host.deny'


def getData():
    with open(resultFile, 'w', encoding="utf8") as file:
        resData = requests.get(
            url, headers=user_agent.getheaders()).content.decode("utf8")
        file.write(resData)

if __name__ == "__main__":
    start_time = time.time()
    getData()
    print("last time: {} s".format(time.time() - start_time))
