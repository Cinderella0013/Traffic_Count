import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# กำหนดประเภทรถ
car_types = [
    "รถยนต์นั่งไม่เกิน 7 ที่นั่ง",
    "รถยนต์นั่งเกิน 7 ที่นั่ง",
    "รถโดยสารขนาดเล็ก",
    "รถโดยสารขนาดกลาง",
    "รถโดยสารขนาดใหญ่",
    "รถปิ๊คอัพส่วนบุคคล",
    "รถบรรทุกขนาดเล็ก",
    "รถบรรทุกขนาดกลาง 6 ล้อ",
    "รถบรรทุกขนาดใหญ่ 10-12 ล้อ",
    "รถพ่วง/รถกึ่งพ่วง",
    "รถบรรทุกกึ่งพ่วง",
    "รถจักรยานยนต์"
]

# สร้าง Dictionary สำหรับเก็บจำนวนรถในแต่ละทิศทาง
traffic_data = {
    'ทิศทางที่ 1': {car_type: 0 for car_type in car_types},
    'ทิศทางที่ 2': {car_type: 0 for car_type in car_types},
    'ทิศทางที่ 3': {car_type: 0 for car_type in car_types},
    'ทิศทางที่ 4': {car_type: 0 for car_type in car_types},
    'ทิศทางที่ 5': {car_type: 0 for car_type in car_types},
    'ทิศทางที่ 6': {car_type: 0 for car_type in car_types}
}

# ฟังก์ชันสำหรับเพิ่มจำนวนรถ
def add_car(direction, car_type):
    traffic_data[direction][car_type] += 1
    update_labels()

# ฟังก์ชันสำหรับลดจำนวนรถ
def subtract_car(direction, car_type):
    if traffic_data[direction][car_type] > 0:
        traffic_data[direction][car_type] -= 1
        update_labels()

# ฟังก์ชันสำหรับรีเซ็ตข้อมูลทั้งหมด
def reset_all():
    for direction in traffic_data:
        for car_type in traffic_data[direction]:
            traffic_data[direction][car_type] = 0
    update_labels()

# ฟังก์ชันสำหรับอัปเดตค่าบนหน้าจอ
def update_labels():
    for direction in traffic_data:
        for car_type in car_types:
            label_text = f"{car_type}: {traffic_data[direction][car_type]}"
            labels[direction][car_type].config(text=label_text)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมนับจำนวนรถ")
root.geometry("1200x700")  # ขนาดเริ่มต้นของหน้าต่าง

# กำหนดฟอนต์ TH Sarabun New
try:
    sarabun_font = tkfont.Font(family="TH Sarabun New", size=14)
except tk.TclError:
    print("Warning: 'TH Sarabun New' font not found. Using default font.")
    sarabun_font = tkfont.Font(family="Helvetica", size=12)

# ตั้งค่าสไตล์
style = ttk.Style()
style.configure("TButton", font=sarabun_font)
style.configure("TLabel", font=sarabun_font)
style.configure("TLabelframe.Label", font=sarabun_font)

# สร้าง frames และ labels
frames = {}
labels = {}

# จัดทิศทางให้แสดงใน 2 แถว 3 คอลัมน์
MAX_ROWS_PER_COLUMN = 6  # จำนวนรายการต่อคอลัมน์ก่อนขึ้นคอลัมน์ใหม่

for i, direction in enumerate(traffic_data.keys()):
    # ตำแหน่งบนหน้าหลัก
    row_num = 0 if i < 3 else 1
    col_num = i if i < 3 else i - 3

    frame = ttk.LabelFrame(root, text=direction, padding=(10, 5))
    frame.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="nsew")

    root.grid_columnconfigure(col_num, weight=1)
    root.grid_rowconfigure(row_num, weight=1)

    frames[direction] = frame
    labels[direction] = {}

    for idx, car_type in enumerate(car_types):
        col = idx // MAX_ROWS_PER_COLUMN
        row = idx % MAX_ROWS_PER_COLUMN

        inner_frame = ttk.Frame(frame, padding=(2, 2))
        inner_frame.grid(row=row, column=col, sticky="ew", padx=2, pady=1)

        add_button = ttk.Button(inner_frame, text="+", width=5,
                                command=lambda d=direction, ct=car_type: add_car(d, ct))
        add_button.pack(side="right", padx=(5, 0))

        subtract_button = ttk.Button(inner_frame, text="-", width=5,
                                     command=lambda d=direction, ct=car_type: subtract_car(d, ct))
        subtract_button.pack(side="right")

        label_text = f"{car_type}: {traffic_data[direction][car_type]}"
        label = ttk.Label(inner_frame, text=label_text)
        label.pack(side="left", expand=True, fill="x")

        labels[direction][car_type] = label

# ปุ่มรีเซ็ต
reset_frame = ttk.Frame(root)
reset_frame.grid(row=2, column=0, columnspan=3, pady=20)

reset_button = ttk.Button(reset_frame, text="รีเซ็ตทั้งหมด", command=reset_all)
reset_button.pack()

# ปรับขนาด layout
root.grid_rowconfigure(2, weight=0)  # รีเซ็ตไม่ต้องขยาย
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
