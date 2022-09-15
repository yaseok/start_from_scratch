# engine apply - ips xff real ip

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_ips_xff_real_ip.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS XFF Real IPv4 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## IPS XFF Real IPv4
* "ATTACK01"에서 "$VS_DUT01.ip"로 XFF Real IP 패킷을 전송한다 (<realip>)
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

## IPS XFF Real IPv6
* "ATTACK01"에서 "$VS_DUT01.vmname"으로 SMAC"$ATTACK01.mac", DMAC"$VS_DUT01.mac", SIPv6"$ATTACK01.ipv6", DIPv6"$VS_DUT01.ipv6"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다 (<logcheck>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)