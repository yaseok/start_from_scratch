# bvtcase 수행

Tags: DEVICE.real_cent.ini
table: data/engine/table_run_bvtcase.csv

## bvtcase 수행
* "VS_DUT01"에서 bvtcase <casename>를 실행한다
* EXEC 실행 결과 메시지는 "TEST done"를 포함 한다

bvtcase 마지막에 엔진, 드라이버를 종료시키는 step이 있어서
다음 spec 수행 전 엔진, 드라이버를 다시 초기화해줘야 함. spec을 끼워넣을지 어찌할지 생각해야봐야함