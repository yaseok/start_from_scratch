# NQPlus 테스트 Spec 2

Tags: DEVICE.vs_cent.ini

## HIPS DUT 시스템 signature sample Test
[STEP 1]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 HIPS 엔진을 초기화 한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* HIPS:"VSDUT01"에서 anse_mon을 데몬 모드로 실행 후 구동상태 확인한다
* HIPS:"VSDUT01"에서 엔진 드라이버를 초기화 한다

[STEP 2]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 anse_ctl를 이용하여 시그니처 엔진을 설정한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "VSDUT01"에서 "cd /ahnlab/anse/autotest/5/test_conf"를 실행한다
* EXEC 실행 결과 코드는 "0"와 같다
* "VSDUT01"에서 "anse_ctl engine apply policy.json infra.json"를 실행한다
* EXEC 실행 결과 코드는 "0"와 같다

* HIPS:"VSDUT01"에서 anse_ctl Tool을 이용하여 엔진 이벤트 파일:"/tmp/result.json"으로 설정한다

[STEP 3]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 NameSpace를 이용하여 시그니처 엔진테스트 환경을 구성한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* HIPS:"VSDUT01"에서 Network Namespace 이름:"test", Local IP:"1.1.1.1", Network Namespace IP:"1.1.1.2", Netmask:"24"로 설정한다

* HIPS:"VSDUT01"에서 NC를 이용하여 포트:"8039"로 백그라운드 프로세스로 Listen한다

[STEP 4]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 NameSpace를 이용하여 탐지 시그니처를 전송한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* HIPS:"VSDUT01"에서 NC를 이용하여 Server IP:"1.1.1.1", Port:"8039"로 접속하여 Content:"GET /T%21E%40S%23T%24 HTTP/1.1\\nHost: Test.Com\\n"를 전송한다


[STEP 5]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 탐지된 json을 확인한다.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* HIPS:"VSDUT01"에서 엔진 이벤트 파일:"/tmp/result.json"을 읽어 Array 형태의 Json:"event_result"으로 저장한다
* Json Name:"event_result"을 보여준다
* Json Name:"event_result"의 XPATH:"[-1].\"event data\".\"attack id\""의 값은 Number value:"100"와 같다
__________________________________________________________________________
* HIPS:"VSDUT01"에서 엔진 드라이버를 종료한다
* HIPS:"VSDUT01"에서 anse_mon을 종료 후 구동상태 확인한다
* HIPS:"VSDUT01"에서 Network Namespace 이름:"test"을 제거한다