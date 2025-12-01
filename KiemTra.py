import Ham
print("Nhap N: ", end= "")
N = Ham.nhapN()

Ham.xuatTG(N)
# Ham.xuatTG1(N)

#====================Bài 11=====================
#==Kiểm tra một số có phải là số hoàn hảo không.==
#(Số hoàn hảo = tổng ước số nhỏ hơn nó = chính nó)
print("Nhap so de kiem tra: ")
So = Ham.nhapN()
if(Ham.soHH(So)):
    print(f"So {So} la so hoan hao!")
else:
    print(f"So {So} khong phai la so hoan hao!")