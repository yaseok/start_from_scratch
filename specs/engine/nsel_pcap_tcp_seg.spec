# engine apply - TCP Segmentation

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_ips_tcp_seg.csv

## TCP Segmentation
* 로컬 파일:"pcap/http_request_encoded_reassembled.pcap"을 Device:"VS_DUT01"의 경로:"/tmp/http_request_encoded_reassembled.pcap"로 업로드 한다
* HIPS:"VS_DUT01"에서 엔진의 설정을 변경하고 적용한다 (Boolean Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* HIPS:"VS_DUT01"에서 엔진의 설정을 확인한다 (Array Type, <anse_cmd>, <result_path>, <result_key_1>, <result_key_2>, <result_value_1>, <result_value_2>, <result_keytype_1>, <result_keytype_2>)
* "VS_DUT01"에서 "$VS_DUT01.interface" 인터페이스를 통해 "http_request_encoded_reassembled.pcap" 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
