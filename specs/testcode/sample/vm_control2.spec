# HYUNSEOK KIM 1

Tags: DEVICE.vs_hyunseok.ini, DEVICE.vsphere.ini

## HYUNSEOK 1
* "ESXI_244"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"NSEL_CentOS7.6_1810"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"NSEL_CentOS7.6_1810"을 SnapShot 이름:"$ss"으로 복구한다
* "ESXI_244"에서 VM:"NSEL_CentOS7.6_1810"의 전원을 켜다
* "ESXI_244"에서 VM:"NSEL_CentOS7.6_1810"의 전원 상태를 확인한다
* EXEC 실행 결과 메시지는 "on"를 포함 한다
* 모든 Device의 연결을 초기화 한다

## HYUNSEOK 2
* "VS_DUT01"에서 "uname -r"를 실행한다
* EXEC 실행 결과 메시지는 "$ss"를 포함 한다