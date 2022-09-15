# vsphere 테스트 환경  테스트

Tags: DEVICE.vox_test.ini, DEVICE.vsphere.ini

table: data/engine_sample/vox_test.csv

## Snapshot Test
* "ESXI_244"에서 VM:"$VSDUT01.vmname"의 Snapshot 이름:<snapshot>을 조건:<doinit>에 따라 복구한다
* HIPS:"VSDUT01"에 엔진 경로:"../NSEL"를 통해 엔진 테스트 환경 초기화 ( 확인:"true", 조건:<doinit> )

* "VSDUT01"에서 "/ahnlab/anse/autotest/run.sh tc_conf_agent_apply"를 실행한다

* HIPS:"VSDUT01"에 엔진 테스트 환경 정리 ( 확인:"true", 조건:<doinit> )
* 테스트 조건이 성공이다

___________________________________________________________________________
* "ESXI_244"에서 테스트 조건에 따라 VM:"$VSDUT01.vmname"의 Snapthot 이름:<snapshot>에 _is_fail 추가해서 생성한다
