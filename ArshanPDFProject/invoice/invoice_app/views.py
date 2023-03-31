from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def invoice(request):
    if request.method == 'POST':
        buyer_name = request.POST.get('buyer_name')
        buyer_address = request.POST.get('buyer_address')
        buyer_phone = request.POST.get('buyer_phone')
        
        seller_name = request.POST.get('seller_name')
        seller_address = request.POST.get('seller_address')
        seller_phone = request.POST.get('seller_phone')

        products = request.POST.get('products')
        price = request.POST.get('price')
        tax = request.POST.get('tax')
        quantity = request.POST.get('quantity')


        products_list = tuple(products.split(', '))
        price_list = tuple(price.split(', '))
        tax_list = tuple(tax.split(', '))
        quantity_list = tuple(quantity.split(', '))

        prds = list(zip(products_list, price_list, tax_list, quantity_list))
        for prd in prds:
            print(prd)
        
        context = {
            'buyer_name': buyer_name,
            'buyer_address': buyer_address,
            'buyer_phone': buyer_phone,
            'seller_name': seller_name,
            'seller_address': seller_address,
            'seller_phone': seller_phone,
            'products': prds,
            'price': price_list,
            'tax': tax_list,
            'quantity': quantity_list,
        }

        return render(request, 'result.html', context)
    return render(request, 'result.html')