from project.admin import admin_modullux
from backend.models import *

from backend.admin.category_admin import *
from backend.admin.product_admin import *

admin_modullux.register(Product, ProductAdmin)
admin_modullux.register(ProductImage, ProductImageAdmin)

admin_modullux.register(Category, CategoryAdmin)
admin_modullux.register(CategoryImage, CategoryImageAdmin)
