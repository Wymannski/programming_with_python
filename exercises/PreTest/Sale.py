class Sale:
    def __init__(self,time:str):
        self.time = time
        self.items : list[SaleLineItem] = []

    def add_item(self,quantity:int,description:str,price:float,item_id:str)->None:
        self.items.append(SaleLineItem(quantity,description,price,item_id))

    def grand_total(self)->float:
        total = 0
        for item in self.items:
            total += item.quantity * item.product_description.price
        return total

class SaleLineItem:
    def __init__(self,quantity:int,description:str,price:float,item_id:str):
        self.quantity = quantity
        self.product_description = ProductDescription(description, price, item_id)

class ProductDescription:
    def __init__(self,description:str,price:float,item_id:str):
        self.description = description
        self.price = price
        self.item_id = item_id

def main():
    try:
        with open('table-settings.txt','r',encoding='UTF-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('file not found')
    if lines:
        sale = Sale("12:00")
        lines = lines[2:]
        for line in lines:
            arr = line.split()
            sale.add_item(int(arr[1]),arr[3],float(arr[2]),arr[1])

        print(sale.grand_total())



if __name__ == '__main__':
    main()






