# TODO: Implement gRPC client (Ngày 2-3)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

import grpc
from generated import school_pb2_grpc
from generated import school_pb2

def run():
    with grpc.insecure_channel('localhost:50053') as channel:
        # ------------------MATH----------------------
        # stub = school_pb2_grpc.MathServiceStub(channel)

        # response1 = stub.TinhTong(
        #     school_pb2.HaiSo(a=5.5, b=4.5)
        # )

        # print(f"Kết quả tổng: {response1.gia_tri}")
        # print(f"Mô tả: {response1.mo_ta}")

        # print("---Next---")

        # response2 = stub.TinhNhanTu(
        #     school_pb2.MotSo(n=12)
        # )

        # print(f"Danh sách ước số: {response2.danh_sach}")
        # print(f"Mô tả: {response2.mo_ta}")

        # ------------------STUDENT----------------------
        # stub = school_pb2_grpc.StudentServiceStub(channel)

        # print("=== Thêm Sinh Viên ===")

        # students = [
        #     ("SV01", "Nguyen Van A", 8.5),
        #     ("SV02", "Tran Thi B", 4.2),
        #     ("SV03", "Le Van C", 6.0),
        # ]

        # for ma_sv, ho_ten, diem in students:
        #     response = stub.ThemSinhVien(
        #         school_pb2.SinhVien(
        #             ma_sv=ma_sv,
        #             ho_ten=ho_ten,
        #             diem=diem
        #         )
        #     )

        #     print(response.thong_bao)

        # print("\n=== Danh Sách Tất Cả ===")

        # response = stub.LayDanhSach(
        #     school_pb2.ThamSo(loc="all")
        # )

        # for sv in response.sinh_viens:
        #     print(f"{sv.ma_sv} | {sv.ho_ten} | {sv.diem}")

        # print("Tổng số:", response.tong_so)

        # print("\n=== Danh Sách Đậu ===")

        # response = stub.LayDanhSach(
        #     school_pb2.ThamSo(loc="pass")
        # )

        # for sv in response.sinh_viens:
        #     print(f"{sv.ma_sv} | {sv.ho_ten} | {sv.diem}")

        # print("Tổng số:", response.tong_so)

        # print("\n=== Danh Sách Rớt ===")

        # response = stub.LayDanhSach(
        #     school_pb2.ThamSo(loc="fail")
        # )

        # for sv in response.sinh_viens:
        #     print(f"{sv.ma_sv} | {sv.ho_ten} | {sv.diem}")

        # print("Tổng số:", response.tong_so)

        # ------------------SYSTEM----------------------
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
        

if __name__ == "__main__":
    run()