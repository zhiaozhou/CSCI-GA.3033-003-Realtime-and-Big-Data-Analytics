#!/usr/bin/env bash

for i in $(seq 1 3)
do
        echo $i
        cat tmp/tmp_input
        hdfs dfs -rm -r tmp_input tmp
        hdfs dfs -put tmp/tmp_input
        
        hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -D mapreduce.job.reduces=1 \
        -files myHW/HW3/HW3_map.py,myHW/HW3/HW3_reduce.py \
        -mapper "python HW3_map.py" \
        -reducer "python HW3_reduce.py" \
        -input hdfs://dumbo/user/zz1749/tmp_input \
        -output hdfs://dumbo/user/zz1749/tmp
        
        rm tmp/pr$(($i-1))
        hdfs dfs -get tmp/part-00000 tmp/pr$i
        cat tmp/pr$i > tmp/tmp_input
        
        cat tmp/tmp_input
done