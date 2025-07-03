import ctypes
import hashlib
import io

def run_responder(cm_port, tcp_port):
    so_path = "/home/wangsheng/Documents/dpu_load/samples/doca_rdma/rdma_write_responder_pool/build/lib_doca_rdma_write_responder.so"
    mylib = ctypes.CDLL(so_path)

    mylib.rdma_write_responder_my.argtypes = [
        ctypes.POINTER(ctypes.c_char),
        ctypes.POINTER(ctypes.c_size_t),
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_size_t
    ]
    mylib.rdma_write_responder_my.restype = ctypes.c_int

    BUF_SIZE = 2048 * 1024 * 1024
    py_buf = ctypes.create_string_buffer(BUF_SIZE)
    actual_size = ctypes.c_size_t(0)
    mem_len = 300 * 1024 * 1024

    ret = mylib.rdma_write_responder_my(py_buf, ctypes.byref(actual_size), cm_port, tcp_port, mem_len)
    received_data = py_buf.raw[:actual_size.value]

    if ret == 0:
        buffer = io.BytesIO(received_data)
        buffer.seek(0)
        hash = hashlib.md5(buffer.read()).hexdigest()
        print(f"[Responder:{cm_port}] 接收到 {actual_size.value} 字节, MD5: {hash}")
    else:
        print(f"[Responder:{cm_port}] 出错，返回值: {ret}")

if __name__ == "__main__":
    run_responder(13600, 18601)