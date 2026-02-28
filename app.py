# app.py
# Thanh vien B — Flask Dashboard
# Nhan request tu browser -> goi ham trong client.py -> tra JSON ve

from flask import Flask, render_template, request, jsonify
import client

app = Flask(__name__)


# ----------------------------------------------------------------
# TRANG CHINH
# ----------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# ----------------------------------------------------------------
# MATH SERVICE
# ----------------------------------------------------------------

@app.route('/api/tinh-tong', methods=['POST'])
def api_tinh_tong():
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"loi": "Thieu tham so a hoac b"}), 400
    try:
        result = client.TinhTong(float(data['a']), float(data['b']))
        return jsonify({"gia_tri": result.gia_tri, "mo_ta": result.mo_ta})
    except Exception as e:
        return jsonify({"loi": f"Khong ket noi MathService: {str(e)}"}), 500


@app.route('/api/nhan-tu', methods=['POST'])
def api_nhan_tu():
    data = request.json
    if not data or 'n' not in data:
        return jsonify({"loi": "Thieu tham so n"}), 400
    try:
        result = client.TinhNhanTu(int(data['n']))
        return jsonify({"danh_sach": list(result.danh_sach), "mo_ta": result.mo_ta})
    except Exception as e:
        return jsonify({"loi": f"Khong ket noi MathService: {str(e)}"}), 500


# ----------------------------------------------------------------
# STUDENT SERVICE
# ----------------------------------------------------------------

@app.route('/api/them-sv', methods=['POST'])
def api_them_sv():
    data = request.json
    for field in ['ma_sv', 'ho_ten', 'diem']:
        if not data or field not in data or str(data[field]).strip() == '':
            return jsonify({"loi": f"Thieu hoac trong truong: {field}"}), 400
    try:
        diem = float(data['diem'])
        if not (0 <= diem <= 10):
            return jsonify({"loi": "Diem phai tu 0.0 den 10.0"}), 400
        result = client.ThemSinhVien(data['ma_sv'], data['ho_ten'], diem)
        return jsonify({"thanh_cong": result.thanh_cong, "thong_bao": result.thong_bao})
    except Exception as e:
        return jsonify({"loi": f"Khong ket noi StudentService: {str(e)}"}), 500


@app.route('/api/danh-sach-sv', methods=['GET'])
def api_danh_sach_sv():
    loc = request.args.get('loc', 'all')
    if loc not in ['all', 'pass', 'fail']:
        return jsonify({"loi": "loc chi chap nhan: all, pass, fail"}), 400
    try:
        result = client.LayDanhSach(loc)
        return jsonify({
            "sinh_viens": [
                {"ma_sv": sv.ma_sv, "ho_ten": sv.ho_ten, "diem": round(sv.diem, 1)}
                for sv in result.sinh_viens
            ],
            "tong_so": result.tong_so
        })
    except Exception as e:
        return jsonify({"loi": f"Khong ket noi StudentService: {str(e)}"}), 500


# ----------------------------------------------------------------
# SYSTEM SERVICE
# ----------------------------------------------------------------

@app.route('/api/trang-thai', methods=['GET'])
def api_trang_thai():
    results = []
    for svc in ['MathService', 'StudentService', 'SystemService']:
        try:
            r = client.KiemTraTrangThai(svc)
            results.append({
                "ten": r.ten_service, "hoat_dong": r.hoat_dong,
                "thoi_gian": r.thoi_gian, "so_yeu_cau": r.so_yeu_cau
            })
        except Exception:
            results.append({
                "ten": svc, "hoat_dong": False,
                "thoi_gian": "Khong phan hoi", "so_yeu_cau": 0
            })
    return jsonify(results)


# ----------------------------------------------------------------
# CHAY APP
# ----------------------------------------------------------------
if __name__ == '__main__':
    print("=" * 50)
    print("  Flask chay tai: http://localhost:5000")
    print("  Dam bao 3 gRPC server dang chay truoc!")
    print("=" * 50)
    app.run(debug=True, port=5000)