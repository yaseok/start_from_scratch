# fw xff real ipv6

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/table_config_fw_xff_real_ipv6.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 방화벽 XFF Real IPv6
* W_HIPS:"W_DUT"에 방화벽 XFF Real IPv6 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다
* "ATTACK"에서 "$W_DUT.ip"으로 SMAC"$ATTACK.mac", DMAC"$W_DUT.mac", SIPv6"$ATTACK.ipv6", DIPv6"$W_DUT.ipv6"인 패킷을 전송한다
* W_HIPS:"W_DUT"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

## 국가기반 XFF Real IPv6
* W_HIPS:"W_DUT"에 국가기반 XFF Real IPv6 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다
* "ATTACK"에서 "$W_DUT.ip"으로 SMAC"$ATTACK.mac", DMAC"$W_DUT.mac", SIPv6"$ATTACK.ipv6", DIPv6"$W_DUT.ipv6"인 패킷을 전송한다
* W_HIPS:"W_DUT"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)