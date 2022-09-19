# product apply - chw build
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/ips_table_predefined_add_1.csv

## 삭제 및 설치
* "P_W_DUT"에서 "cd 'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/AhnLab/AhnLab Host IPS'"를 실행한다
* "P_W_DUT"에서 "cp './AhnLab Host IPS 제거.lnk' c:/var/"를 실행한다
* "P_W_DUT"에서 "cd 'c:/var'"를 실행한다
* "P_W_DUT"에서 "& './AhnLab Host IPS 제거.lnk' /s"를 실행한다
\* "P_W_DUT"에서 "./AhnLab Host IPS 제거.lnk /s"를 실행한다
* 15초 동안 대기
* "P_W_DUT"에서 "rm 'C:/var/AhnLab Host IPS 제거.lnk'"를 실행한다

## 설치
* "P_W_DUT"에서 "cd 'c:/var/setup'"를 실행한다
\* "P_W_DUT"에서 "& './hips_setup.exe' /s"를 실행한다
* "P_W_DUT"에서 "./hips_setup.exe /s"를 실행한다
* 30초 동안 대기

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup - 정책적용 (fail시 미설치 판단)
* P_W_HIPS:"P_W_DUT"에 IPS 테스트를 위한 설정을 수행한다





