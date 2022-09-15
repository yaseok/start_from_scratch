from getgauge.python import step, data_store
from nqplus.gocdlib.utils import nq_exec, nq_read_on_remote
from nqplus.gocdlib.nq_json_util import jname
import json, sys, re

@step("W_HIPS:<devicename>에서 anse_ctl Tool을 이용하여 엔진 설정 파일:<filename>을 적용한다")
def step_impl( devicename, filename ):
    shell_cmd = "./anse_ctl -j engine apply %s"%( filename )
    nq_exec( devicename, shell_cmd )

@step("W_HIPS:<devicename>에서 anse_ctl Tool을 이용하여 <command> 명령을 수행한다")
def step_impl( devicename, command):
    shell_cmd = "./anse_ctl -j %s"%( command )
    nq_exec( devicename, shell_cmd )
