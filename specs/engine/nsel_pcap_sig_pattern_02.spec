# 시그니처 패턴 별 검증 02

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_nsel_sig_pattern_02.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 신규 시그니처 옵션 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## 시그니처 패턴 별 탐지/미탐 동작 확인
* 로컬 파일:<src>을 Device:"VS_DUT01"의 경로:<dst>로 SCP 복사 한다
* HIPS:"VS_DUT01"에서 엔진의 설정을 변경하고 적용한다_신규 시그니처 옵션 (<path_remote>)
* "VS_DUT01"에서 "$VS_DUT01.interface" 인터페이스를 통해 <pcap> 패킷을 전송한다
* HIPS:"VS_DUT01"에서 시그니처 패턴 별 이벤트 로그를 확인한다 (<logcheck>, <log_key>, <log_keytype>, <log_value>)