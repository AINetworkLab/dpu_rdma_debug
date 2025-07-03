import ctypes
import os

# 加载共享库
# 根据你的实际路径修改
lib_path = os.path.abspath('/home/wangsheng/load/samples/doca_rdma/rdma_write_requester_pool_th/build/lib_doca_rdma_write_requester.so')
lib = ctypes.CDLL(lib_path)

# 定义 my_main 函数的返回类型
lib.my_main.restype = ctypes.c_int

if __name__ == "__main__":
    print("调用 my_main 函数...")
    
    # 直接调用 my_main 函数
    result = lib.my_main()
    
    print(f"my_main 函数返回值: {result}")
    
    if result == 0:
        print("函数执行成功!")
    else:
        print(f"函数执行失败，错误码: {result}")