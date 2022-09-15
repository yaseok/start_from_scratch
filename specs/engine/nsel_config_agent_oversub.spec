# engine apply - agent_oversub

Tags: DEVICE.real_cent.ini
table: data/engine/table_config_agent_engine_oversub.csv

## engine oversubscription

현재 oversubscription 기능을 검증할 트래픽 생성이 어려워 설정 변경, 적용 여부만 확인합니다.

* HIPS:"VS_DUT01"에서 엔진의 설정을 변경하고 적용한다 (Boolean Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* HIPS:"VS_DUT01"에서 엔진의 설정을 확인한다 (Array Type, <anse_cmd>, <result_path>, <result_key_1>, <result_key_2>, <result_value_1>, <result_value_2>, <result_keytype_1>, <result_keytype_2>)