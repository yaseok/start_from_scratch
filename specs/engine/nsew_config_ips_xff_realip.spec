# ips xff real ip

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/table_config_ips_xff_real_ip.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 IPS XFF Real IPv4 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## IPS XFF Real IPv4
* "ATTACK"에서 "$W_DUT.ip"로 XFF Real IP 패킷을 전송한다 (<realip>)
* W_HIPS:"W_DUT"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
* "W_DUT"에서 "C:/tmp/./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## IPS XFF Real IPv6
* "ATTACK"에서 "$W_DUT.ip"으로 SMAC"$ATTACK.mac", DMAC"$W_DUT.mac", SIPv6"$ATTACK.ipv6", DIPv6"$W_DUT.ipv6"인 패킷을 전송한다
* W_HIPS:"W_DUT"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)