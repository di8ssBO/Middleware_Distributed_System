# TODO: Implement gRPC client (Ngày 2-3)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

import grpc
from generated import school_pb2_grpc
from generated import school_pb2

# Math Service
def TinhTong(a, b):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = school_pb2_grpc.MathServiceStub(channel)
        response = stub.TinhTong(school_pb2.HaiSo(a=a, b=b))
        return response.gia_tri

def TinhNhanTu(n):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = school_pb2_grpc.MathServiceStub(channel)
        response = stub.TinhNhanTu(school_pb2.MotSo(n=n))
        return response.gia_tri

# Student Service
def ThemSinhVien(students):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = school_pb2_grpc.StudentServiceStub(channel)

        # students = [
        #     ("SV01", "Nguyen Van A", 8.5),
        #     ("SV02", "Tran Thi B", 4.2),
        #     ("SV03", "Le Van C", 6.0),
        # ]

        for ma_sv, ho_ten, diem in students:
            response = stub.ThemSinhVien(
                school_pb2.SinhVien(
                    ma_sv=ma_sv,
                    ho_ten=ho_ten,
                    diem=diem
                )
            )

            print(response.thong_bao)

def DanhSachDau():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = school_pb2_grpc.StudentServiceStub(channel)

        response = stub.LayDanhSach(
            school_pb2.ThamSo(loc="pass")
        )

        for sv in response.sinh_viens:
            print(f"{sv.ma_sv} | {sv.ho_ten} | {sv.diem}")

        print("Tổng số:", response.tong_so)

def DanhSachRot():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = school_pb2_grpc.StudentServiceStub(channel)

        response = stub.LayDanhSach(
            school_pb2.ThamSo(loc="fail")
        )

        for sv in response.sinh_viens:
            print(f"{sv.ma_sv} | {sv.ho_ten} | {sv.diem}")

        print("Tổng số:", response.tong_so)

# System Service
def KiemTraTrangThai():
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = school_pb2_grpc.SystemServiceStub(channel)

        services = ["MathService", "StudentService", "SystemService"]

        for name in services:
            response = stub.KiemTraTrangThai(
                school_pb2.YeuCau(ten_service=name)
            )

            print(f"\nService: {response.ten_service}")
            print("Hoạt động:", response.hoat_dong)
            print("Thời gian:", response.thoi_gian)
            print("Số yêu cầu kiểm tra:", response.so_yeu_cau)

def run():
    choice = int(input("Nhập lựa chọn (1 - Math, 2 - Student, 3 - System): "))

    if choice == 1:
        # MATH
        print(TinhTong(4, 5))
    elif choice == 2:
        # STUDENT
        students = [
            ("SV01", "Nguyen Van A", 8.5),
            ("SV02", "Nguyen Van B", 7.5),
            ("SV03", "Nguyen Van C", 4)
        ]
        ThemSinhVien(students)
        DanhSachDau()
    else: 
        # SYSTEM
        KiemTraTrangThai()    

if __name__ == "__main__":
    run()