from getgauge.python import step
from nqplus.gocdlib.utils import nq_exec, nq_exec_check_code
import time

from nqplus.gocdlib.utils import nq_exec, nq_exec_get_result_message
from nq.logging import logger
import re
import json
from nqplus.gocdlib.nq_json_util import create_json

@step("<attack_device>에서 <hips_device>로 Signature가 <content>이고 TCP 출발지 포트 1000 및 목적지 포트가 <port>인 패킷을 전송함")
def step_impl( attack_device, hips_device, content, port ):
    shell_cmd = "hping3 %s -e \"%s\" -p %s -s 1000 -c 1"%(hips_device, content, port)
    nq_exec( attack_device, shell_cmd )  

@step("<attack_device>에서 <hips_device>로 Signature가 <content>이고 출발지 IP가 1.0.1.1 인 패킷을 전송함")
def step_impl( attack_device, hips_device, content ):
    shell_cmd = "hping3 %s -e \"%s\" -a 1.0.1.1 -c 1"%(hips_device, content)
    nq_exec( attack_device, shell_cmd )  

def get_hips_evt_log( fullmsg ):
    LOG_DATE=r"^\[\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\]"
    LOG_T1=r"\[p\d+\]"
    LOG_T2=r"\[t\d+\]"
    LOG_T3=r"\[e0x[0-9A-Fa-f]+\]"
    LOG_C1=r" _\$M_EMSServerProxyLib_\$L_"
    EVT_LOG=r"(.*)"
    LOG_HEADER=LOG_DATE+LOG_T1+LOG_T2+LOG_T3+LOG_C1+EVT_LOG

    reqjsonlist=list()

    reqlinelist=list()
    reslinelist=list()
    status = 0
    REQ_ETC=r"_RequestHttpServerViaPOST request"
    REQ_HEADER=r"\[REQUEST Json\]"
    RES_HEADER=r"\[RESPONSE Json\]"
    for line in fullmsg.splitlines():
        if re.match(LOG_HEADER, line):
           l = re.match(LOG_HEADER, line).group(1)
        else:
           l = line

        if re.match( REQ_ETC, l):
           status=0
           continue
        elif re.match( REQ_HEADER, l):
           status=1
           continue
        elif re.match( RES_HEADER, l):
           status=2
           reqjsonlist.append( "\n".join(reqlinelist) )
           reqlinelist=list()
           continue
        else:
           logger.debug("data:%s"%(l))

        if status == 1:
           reqlinelist.append(l)
        else:
           logger.debug("skip:%s"%(l))

    return reqjsonlist

@step("<devicename>에서 로그파일: <logfile>에서 Json Request만 출력한다")
def print_winlog( devicename, logfile ):
    nq_exec( devicename, "Get-Content %s"%logfile )
    mixed_msg=nq_exec_get_result_message()
    result_json=get_hips_evt_log(mixed_msg)
    print(result_json[0])

@step("<devicename>에서 로그파일: <logfile>에서 Json Name:<jsonname>으로 생성한다")
def print_winlog( devicename, logfile, jsonname ):
    nq_exec( devicename, "Get-Content %s"%logfile )
    mixed_msg=nq_exec_get_result_message()
    jsonlists=get_hips_evt_log(mixed_msg)
    jsonresult=list()
    for item in jsonlists:
        logger.debug("Jaon data:(%s) load"%(item))
        jitem = json.loads(item.replace("\n",""))
        jsonresult.append(jitem)
    create_json( jsonname, jsonresult )
    logger.debug("Jsonname:(%s)으로 Json data:(%s)생성"%(jsonname, jsonresult))

@step("30초 동안 대기")
def step_impl():
    time.sleep(30)

@step("60초 동안 대기")
def step_impl():
    time.sleep(60)

@step("90초 동안 대기")
def step_impl():
    time.sleep(90)

@step("120초 동안 대기")
def step_impl():
    time.sleep(120)

@step("<attack_device>에서 <hips_device>로 Signature가 <content>이고 출발지 IP가 1.0.1.1 인 패킷을 전송함1")
def step_impl( attack_device, hips_device, content ):
    shell_cmd = "hping3 %s -e \"%s\" -a 1.0.1.1 -c 1"%(hips_device, content)
    nq_exec( attack_device, shell_cmd )  