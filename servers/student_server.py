import grpc
from concurrent import futures
import time

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'generated'))

import school_pb2
import school_pb2_grpc

class StudentService(school_pb2_grpc.StudentServiceServicer):

    def __init__(self):
        self.students = []

    def ThemSinhVien(self, request, context):
        for sv in self.students:
            if sv.ma_sv == request.ma_sv:
                return school_pb2.PhanHoi(
                    thanh_cong=False,
                    thong_bao=f"Sinh viên {request.ma_sv} đã tồn tại"
                )
        
        self.students.append(request)

        return school_pb2.PhanHoi(
            thanh_cong=True,
            thong_bao=f"Đã thêm sinh viên {request.ma_sv}"
        )
    
    def LayDanhSach(self, request, context):
        filter_type = request.loc.lower()

        if filter_type == "all":
            filtered = self.students
        elif filter_type == "pass":
            filtered = [sv for sv in self.students if sv.diem >= 5]
        elif filter_type == "fail":
            filtered = [sv for sv in self.students if sv.diem < 5]
        else:
            filtered = []
    
        return school_pb2.DanhSachSV(
            sinh_viens=filtered,
            tong_so=len(filtered)
        )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    school_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)

    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server is running on port 50052")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()