# 시그니처 정책 파일 추출
Tags: DEVICE.nsew_go_server.ini, DEVICE.nsew_attacker.ini

## 신규 시그니처 NSEW Attacker(linux)에 파일 전송
* "W_GO_Server"에서 " cd /root/HIPS_Agent/Agent01/pipelines/01_Trigger/"를 실행한다
* "W_GO_Server"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no SIG/hips_signature.zip root@192.168.181.253:/root/kjcho/signature_db_check/rule/hips_signature.zip"를 실행한다
* "ATTACK"에서 "cd /root/kjcho/signature_db_check/rule"를 실행한다
* "ATTACK"에서 "unzip hips_signature.zip"를 실행한다
* "ATTACK"에서 "../make_hips_policy_2.sh hips_signature_meta.json hips_signature_policy.json"를 실행한다

