# #!/bin/bash

# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate cuda_env

# # 清空 log.txt
# > log.txt

# # 所有输出都写入 log.txt（追加方式），& 表示后台运行
# python3 responder_1.py >> log.txt 2>&1 &
# python3 responder_2.py >> log.txt 2>&1 &
# python3 responder_3.py >> log.txt 2>&1 &
# python3 responder_4.py >> log.txt 2>&1 &

# wait

#!/bin/bash

# 默认日志文件名
DEFAULT_LOG="log.txt"

# 解析参数
LOG_FILE=${1:-$DEFAULT_LOG}

source ~/miniconda3/etc/profile.d/conda.sh
conda activate cuda_env

# 清空日志文件
> "$LOG_FILE"

# 所有输出都写入指定的日志文件
python3 responder_1.py >> "$LOG_FILE" 2>&1 &
python3 responder_2.py >> "$LOG_FILE" 2>&1 &
python3 responder_3.py >> "$LOG_FILE" 2>&1 &
python3 responder_4.py >> "$LOG_FILE" 2>&1 &

wait

echo "所有进程已完成，日志已写入: $LOG_FILE"