import grpc
from concurrent import futures
import time
import socket
from datetime import datetime

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from generated import school_pb2
from generated import school_pb2_grpc

SERVICE_PORTS = {
    "MathService": 50051,
    "StudentService": 50052,
    "SystemService": 50053,
}

class SystemService(school_pb2_grpc.SystemServiceServicer):

    def __init__(self):
        self.request_count = 0

    def KiemTraTrangThai(self, request, context):
        self.request_count += 1

        service_name = request.ten_service
        port = SERVICE_PORTS.get(service_name)

        is_active = False

        if port:
            is_active = self.check_port("localhost", port)

        return school_pb2.TrangThai(
            ten_service=service_name,
            hoat_dong=is_active,
            thoi_gian=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            so_yeu_cau=self.request_count
        )

    def check_port(self, host, port):
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except:
            return False

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    school_pb2_grpc.add_SystemServiceServicer_to_server(
        SystemService(),
        server
    )

    server.add_insecure_port('[::]:50053')
    server.start()
    print("Server is running on port 50053")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()