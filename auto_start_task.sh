#!/bin/bash

# 指定GPU空闲阈值（单位：秒）
IDLE_THRESHOLD=300
echo $IDLE_THRESHOLD

# 从命令行参数获取要执行的脚本文件
SCRIPT_FILE=$1

while true; do
    # 使用nvidia-smi命令获取GPU的使用率
    GPU_USAGE=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits | head -n 1 | awk '{ print $1 }')

    if (( GPU_USAGE < 10 )); then  # 假设GPU使用率低于10%表示空闲
        if (( IDLE_START == 0 )); then
            IDLE_START=$(date +%s)
        fi

        IDLE_TIME=$(( $(date +%s) - $IDLE_START ))

        if (( IDLE_TIME > IDLE_THRESHOLD )); then
            bash $SCRIPT_FILE
            IDLE_START=0
            exit  # 结束脚本的运行
        fi
    else
        IDLE_START=0
    fi

    sleep 1
done
