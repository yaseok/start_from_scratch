# engine apply - XFF

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_ips_xff.csv

## X-Forwarded-For
* 로컬 파일:"pcap/x-forwarded_no_show.pcap"을 Device:"VS_DUT01"의 경로:"/tmp/x-forwarded_no_show.pcap"로 SCP 복사 한다
* 로컬 파일:"data/engine/policy_xff.json"을 Device:"VS_DUT01"의 경로:"/tmp/policy_xff.json"로 SCP 복사 한다
* 로컬 파일:"data/engine/infra_xff.json"을 Device:"VS_DUT01"의 경로:"/tmp/infra_xff.json"로 SCP 복사 한다
* "VS_DUT01"에서 "anse_ctl engine apply /tmp/policy_xff.json /tmp/infra_xff.json"를 실행한다
* EXEC 실행 결과 코드는 "0"와 같다
* "VS_DUT01"에서 "$VS_DUT01.interface" 인터페이스를 통해 "x-forwarded_no_show.pcap" 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
