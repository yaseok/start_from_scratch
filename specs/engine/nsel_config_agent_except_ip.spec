# engine apply - agent except ip

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_except_ip.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 Except IP 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## IPv4 탐지 이벤트 발생
* "ATTACK01"에서 "$VS_DUT01.ip"로 Signature가 "kimhyunseok"이고 TCP 목적지 포트가 "80"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck1>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

## IPv6 탐지 이벤트 발생
* "ATTACK01"에서 "$VS_DUT01.vmname"으로 SMAC"$ATTACK01.mac", DMAC"$VS_DUT01.mac", SIPv6"$ATTACK01.ipv6", DIPv6"$VS_DUT01.ipv6"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다 (<logcheck1>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)
* HIPS:"VS_DUT01"에 Except IP 테스트를 위한 에이전트 설정 파일을 저장하고 설정을 적용한다

## IPv4 탐지 이벤트 미발생
* "ATTACK01"에서 "$VS_DUT01.ip"로 Signature가 "kimhyunseok"이고 TCP 목적지 포트가 "80"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck2>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

## IPv6 탐지 이벤트 미발생
* "ATTACK01"에서 "$VS_DUT01.vmname"으로 SMAC"$ATTACK01.mac", DMAC"$VS_DUT01.mac", SIPv6"$ATTACK01.ipv6", DIPv6"$VS_DUT01.ipv6"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다 (<logcheck2>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)
