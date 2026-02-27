import grpc
from concurrent import futures
import time

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'generated'))

import school_pb2
import school_pb2_grpc

class MathService(school_pb2_grpc.MathServiceServicer):

    def TinhTong(self, request, context):
        result = request.a + request.b

        return school_pb2.KetQua(
            gia_tri=result,
            mo_ta=f"Tổng của {request.a} và {request.b} là {result}"
        )

    def TinhNhanTu(self, request, context):
        n = request.n
        divisors = []

        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)

        return school_pb2.DanhSachSo(
            danh_sach=divisors,
            mo_ta=f"Ước của {n}"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    school_pb2_grpc.add_MathServiceServicer_to_server(MathService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()