# NQPlus 테스트 Spec 2

Tags: DEVICE.vs_cent.ini, DEVICE.vsphere.ini

|INDEX	|Snapshot	|
|-------|---------------|
|1	|auto_test_1.0|


* "ESXI_244"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"Guage_Ubuntu16.04"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"Guage_Ubuntu16.04"을 SnapShot 이름:<Snapshot>으로 복구한다

## HIPS DUT 시스템 Sample 테스트
[STEP 1]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 HIPS 엔진을 업로드하고 패키지를 설치한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* 모든 Device의 연결을 초기화 한다
* HIPS:"VSDUT01"에서 anse 엔진 드라이버 패키지를 설치한다
* HIPS:"VSDUT01"에서 anse testsuite 패키지를 설치한다

* HIPS:"VSDUT01"에서 환경변수 업데이트한다

* HIPS:"VSDUT01"에서 anse_mon을 데몬 모드로 실행 후 구동상태 확인한다
* HIPS:"VSDUT01"에서 anse_mon을 종료 후 구동상태 확인한다


* HIPS:"VSDUT01"에서 anse_mon을 데몬 모드로 실행 후 구동상태 확인한다
* HIPS:"VSDUT01"에서 엔진 드라이버를 초기화 한다
* HIPS:"VSDUT01"에서 엔진 드라이버를 종료한다
* HIPS:"VSDUT01"에서 anse_mon을 종료 후 구동상태 확인한다

* HIPS:"VSDUT01"에서 anse 엔진 드라이버 패키지를 삭제한다
* HIPS:"VSDUT01"에서 anse testsuite 패키지를 삭제한다
