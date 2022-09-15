# 확인한 디버그 정보 가공, 저장
Tags: DEVICE.HIPS.ini, DEVICE.DataStore.ini

## 기존 data를 다운로드 한다
* LOCAL에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no root@192.168.44.93:/data/report_data/HIPS/info_validity.csv data/info_validity.csv"를 실행한다

## 테스트 수행 일자, 엔진 버전, 시그니처 버전 및 규칙 개수를 확인한다
* "HIPS"에서 테스트 수행 일자를 확인한다
* 저장된 "date"를 확인한다

* "HIPS"에서 "anse_ctl engine status |grep data"를 실행한다
* "HIPS"에서 로딩된 HIPS 엔진 버전을 확인한다
* 저장된 "engine_version"를 확인한다

* "HIPS"에서 "anse_ctl core show-sig-version"를 실행한다
* "HIPS"에서 로딩된 HIPS 시그니처 규칙 버전을 확인한다
* 저장된 "sig_version"를 확인한다

* "HIPS"에서 "anse_ctl core show-sig-count"를 실행한다
* "HIPS"에서 로딩된 HIPS 시그니처 규칙 개수를 확인한다
* 저장된 "sig_count"를 확인한다

* 테스트 수행일자 "date"와 수집된 "engine_version", "sig_version", "sig_count", "result"를 파일에 기록한다

## 시그니처 빌드 결과를 확인한다
* "HIPS"에서 "echo [BUILD RESULT] > /tmp/info_build.txt"를 실행한다
* "HIPS"에서 "anse_ctl core show-sig-count >> /tmp/info_build.txt"를 실행한다
* "HIPS"에서 "echo >> /tmp/info_build.txt"를 실행한다
* "HIPS"에서 "echo >> /tmp/info_build.txt"를 실행한다
* "HIPS"에서 "echo [BUILD DEBUG LOG] >> /tmp/info_build.txt"를 실행한다
* "HIPS"에서 "anse_ctl core show-signature-debug error >> /tmp/info_build.txt"를 실행한다

## 추가한 local data를 리포트 생성을 위해 업로드 한다
* "HIPS"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no /tmp/deleted_result.txt root@192.168.44.93:/data/report_data/HIPS/info_deleted_items.txt"를 실행한다
* "HIPS"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no /tmp/required_result.txt root@192.168.44.93:/data/report_data/HIPS/info_required_items.txt"를 실행한다
* "HIPS"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no /tmp/info_build.txt root@192.168.44.93:/data/report_data/HIPS/info_build.txt"를 실행한다
* LOCAL에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no data/info_validity.csv root@192.168.44.93:/data/report_data/HIPS/info_validity.csv"를 실행한다