# nsew package setup

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/w_table_config_fw_enable.csv

\## 기본 Setup
\* W_HIPS:"W_DUT"에 NSEW 패치키를 위치시킨다.

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.


\## Host sweep - 한대로 묶을라고 작업하는거
\## 기본 Setup
\* W_HIPS:"W_DUT"에 IPS Host Sweep 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

\## 기본 방화벽 fw_basic
\* P_W_"ATTACK"에서 IPS 신규 시그니처 옵션 테스트의 탐지 트래픽을 발생시킨다 (<traffic_protocol1>)
\* P_W_"W_DUT"에서 Host Sweep 테스트의 탐지 트래픽을 발생시킨다 (<dip>, <traffic_protocol1>)
\* 3초 동안 대기
\* W_HIPS:"W_DUT"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)






