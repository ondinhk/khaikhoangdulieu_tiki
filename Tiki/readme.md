Cách làm: do cấu trúc API của tiki dựa trên các ID để trả về dữ liệu -> Do đó mục tiêu là tìm được danh sách các ID sản
phẩm của Tiki

-> Tìm API -> phân tích cú pháp

-> Lấy id của 41 danh mục bằng cách cào thủ công link trên tiki -> Sau đó cắt ID danh mục ra dựa trên url.

-> Dựa trên các danh mục tiếp tục lấy cái ID sản phẩm, thu được 75290 id

-> Lọc lại các ID có comment còn lại 51695 sản phẩm

-> Tách thành 4 file, sử dụng 4 thread để giảm thời gian lấy dữ liệu

-> Gọi API lấy comment 
