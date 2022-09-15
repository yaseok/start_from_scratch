# port scan test

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 Port Scan 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## SYN Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 SYN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200001"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다


## ACK Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 ACK Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200002"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## FIN Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 FIN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200003"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## NULL Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 NULL Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200004"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## XMAS Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 XMAS Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200005"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## Stealth Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 Stealth Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200006"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## SYN FIN Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 SYN FIN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200007"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## UDP Port Scan 동작 확인
* W_"ATTACK"에서 "$W_DUT.ip"로 UDP Port Scan 패킷을 전송한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200101"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다
