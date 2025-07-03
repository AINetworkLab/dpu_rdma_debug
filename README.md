# dpu_rdma_debug
./requester
├── daemon_hugepages.c # First, allocate 1GB of hugepages memory.
├── doca_hp_sender.py # The entry point of the .so file used by the requester to invoke RDMA.
├── doca_hp_shm.c # Manage reuse or create a new mmap.
├── doca_hp_shm.h
├── meson.build
├── rdma_common_pool.c # Correspond to rdma_common.c in the sample code.
├── rdma_common_pool.h
├── rdma_control_enum.c # Replaces the wait_for_enter() function with TCP-based management logic.
├── rdma_control_enum.h
├── rdma_write_requester_my.c
├── rdma_write_requester_sample.c
└── time_utils.h
