# train log 
NCCL_DEBUG=INFO         #  打印明确的警告消息以及基本的 NCCL 初始化信息
NCCL_DEBUG_SUBSYS=COLL	#  打印集合调用的日志，这对于调试挂起很有帮助，尤其是由集合类型或消息大小不匹配引起的挂起。
NCCL_DEBUG_SUBSYS=GRAPH	#  如果拓扑检测失败，设置将有助于检查详细的检测结果，并在需要 NCCL 团队进一步帮助时保存作为参考。
