#! /bin/bash
# made by hyunseok.kim1

for vm in $(cat vm.txt)
	do
		for ss in $(cat new.txt)
			do
				vim-cmd vmsvc/snapshot.get $vm |grep $ss > /dev/null
				result=$(echo $?)
				name=$(vim-cmd vmsvc/getallvms |grep $vm | awk '{print $2}')
				if [ $result -eq 0 ];then
				echo "$ss" >> $name
				else
				:
				fi
			done
	done
