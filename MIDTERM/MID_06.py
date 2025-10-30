class Inventory:
    stock=0
    def __init__(self):
        print("새 상품이 등록되었습니다.")

    def get_stock(self):
        return self.stock
    
    def set_stock(self, n):
        return self.stock+n

    def add_stock(self, n):
        if n < 0:
            print("0보다 큰 수량만 입고 가능합니다.")
        else:
            self.stock += n
            print(n,"개가 입고되었습니다.")

    def remove_stock(self, n):
        if n <= 0:
            return
        if n > self.stock:
            print("현재 재고보다 많은 수량은 출고 불가")

            return
        self.stock -= n

item1=Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:",item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())