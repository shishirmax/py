import Selector
sel = Selector(text='<div class="product product-small">I am a product!</div>')
print sel.css('.product').extract()