# engine apply - port scan test

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini

## 기본 Setup
* HIPS:"VS_DUT01"에 Port Scan 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## SYN Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 SYN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200001"를 포함한다

## ACK Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 ACK Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200002"를 포함한다

## FIN Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 FIN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200003"를 포함한다

## NULL Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 NULL Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200004"를 포함한다

## XMAS Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 XMAS Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200005"를 포함한다

## Stealth Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 Stealth Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200006"를 포함한다

## SYN FIN Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 SYN FIN Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200007"를 포함한다

## UDP Port Scan 동작 확인
* "ATTACK01"에서 "$VS_DUT01.ip"로 UDP Port Scan 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json"를 실행한다
* EXEC 실행 결과 메시지는 "11200101"를 포함한다
