class PrinterError(RuntimeError):
    pass


class print():
    def __init__(self,page_per_s,capacity):
        self.page_per_s=page_per_s
        self.capacity=capacity
    
    def prinitng(self,pages):
        if self.capacity<pages:
            raise PrinterError(f"Your capcity is less")
        
        self.capacity=self.capacity-pages
        
        return f"Printer {pages} page in {pages/self.page_per_s:.2f} seconds"
        
        
        