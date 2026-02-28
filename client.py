# client.py
# Thanh vien B dung file nay de goi cac gRPC server cua Thanh vien A
# Moi ham duoi day duoc goi truc tiep tu app.py (Flask)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

import grpc
from generated import school_pb2, school_pb2_grpc


# ================= MATH =================
def TinhTong(a, b):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = school_pb2_grpc.MathServiceStub(channel)
        return stub.TinhTong(school_pb2.HaiSo(a=float(a), b=float(b)))


def TinhNhanTu(n):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = school_pb2_grpc.MathServiceStub(channel)
        return stub.TinhNhanTu(school_pb2.MotSo(n=int(n)))


# ================= STUDENT =================
def ThemSinhVien(ma_sv, ho_ten, diem):
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = school_pb2_grpc.StudentServiceStub(channel)
        return stub.ThemSinhVien(
            school_pb2.SinhVien(ma_sv=ma_sv, ho_ten=ho_ten, diem=diem)
        )


def LayDanhSach(loc="all"):
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = school_pb2_grpc.StudentServiceStub(channel)
        return stub.LayDanhSach(school_pb2.ThamSo(loc=loc))


# ================= SYSTEM =================
def KiemTraTrangThai(ten_service):
    with grpc.insecure_channel("localhost:50053") as channel:
        stub = school_pb2_grpc.SystemServiceStub(channel)
        return stub.KiemTraTrangThai(
            school_pb2.YeuCau(ten_service=ten_service)
        )