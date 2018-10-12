from backend.models import *
from project.admin import admin_modullux

from .category_admin import *
from .furniture_admin import *

admin_modullux.register(Furniture, FurnitureAdmin)
admin_modullux.register(FurnitureImage, FurnitureImageAdmin)

admin_modullux.register(Category, CategoryAdmin)
admin_modullux.register(CategoryImage, CategoryImageAdmin)
