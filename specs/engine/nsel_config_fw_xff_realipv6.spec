# engine apply - xff real ipv6

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_fw_xff_real_ipv6.csv

## 방화벽 XFF Real IPv6
* HIPS:"VS_DUT01"에 방화벽 XFF Real IPv6 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다
* "ATTACK01"에서 "$VS_DUT01.vmname"으로 SMAC"$ATTACK01.mac", DMAC"$VS_DUT01.mac", SIPv6"$ATTACK01.ipv6", DIPv6"$VS_DUT01.ipv6"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

## 국가기반 XFF Real IPv6
* HIPS:"VS_DUT01"에 국가기반 XFF Real IPv6 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다
* "ATTACK01"에서 "$VS_DUT01.vmname"으로 SMAC"$ATTACK01.mac", DMAC"$VS_DUT01.mac", SIPv6"$ATTACK01.ipv6", DIPv6"$VS_DUT01.ipv6"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_4>, <log_keytype_4>, <log_value_4>, <log_key_5>, <log_keytype_5>, <log_value_5>, <log_key_6>, <log_keytype_6>, <log_value_6>)