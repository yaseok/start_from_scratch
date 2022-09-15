# NQPlus 테스트 Spec 2

Tags: DEVICE.real_cent.ini

## HIPS 샘플 Test

[STEP 1]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 HIPS 엔진을 업로드하고 패키지를 설치한다
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* HIPS:"VSDUT01"에서 anse 엔진 드라이버 패키지를 설치한다
* HIPS:"VSDUT01"에서 anse testsuite 패키지를 설치한다

* HIPS:"VSDUT01"에서 anse_mon을 데몬 모드로 실행 후 구동상태 확인한다
* HIPS:"VSDUT01"에서 엔진 드라이버를 초기화 한다

* HIPS:"VSDUT01"에서 엔진의 구동모드 확인시 "normal"이다

* HIPS:"VSDUT01"에서 엔진의 구동모드를 "TAP"로 변경한다
* HIPS:"VSDUT01"에서 엔진의 구동모드 확인시 "tap"이다

* HIPS:"VSDUT01"에서 엔진의 구동모드를 "BYPASS"로 변경한다
* HIPS:"VSDUT01"에서 엔진의 구동모드 확인시 "bypass"이다

* HIPS:"VSDUT01"에서 엔진 드라이버를 종료한다
* HIPS:"VSDUT01"에서 anse_mon을 종료 후 구동상태 확인한다

* HIPS:"VSDUT01"에서 anse 엔진 드라이버 패키지를 삭제한다
* HIPS:"VSDUT01"에서 anse testsuite 패키지를 삭제한다
