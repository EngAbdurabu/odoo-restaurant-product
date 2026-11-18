# Restaurant Product | منتج المطعم

[English](#english) | [العربية](#العربية)

---

## English

### Overview

**Restaurant Product** is a custom Odoo module that extends the standard `product.template` model with additional information useful for managing restaurant products and meals.

### Features

- Adds a **Product Weight** field.
- Adds a **Product Calories** field.
- Adds a **Product Expiration Date** field.
- Displays the additional information in the product form view.
- Displays product weight and expiration date in the product Kanban view.
- Adds a search filter for products with a weight greater than `200`.
- Adds a **Large Meals** menu item that opens products with the weight filter applied by default.

### Technical details

| Item | Details |
|---|---|
| Module name | `restaurant_product` |
| Display name | Restaurant Product |
| Version | `1.0.0` |
| Odoo model extended | `product.template` |
| Dependencies | `product`, `sale` |
| Main files | `models.py`, `views.xml`, `__manifest__.py` |

### Installation

1. Copy the `restaurant_product` folder into your Odoo custom addons directory.
2. Make sure that the custom addons directory is included in your Odoo `--addons-path`.
3. Restart the Odoo server.
4. Enable Developer Mode if needed, then open **Apps**.
5. Update the Apps List.
6. Search for **Restaurant Product** and install it.

Example command (adjust the database name and paths for your environment):

```bash
python odoo-bin -d YOUR_DATABASE --addons-path=addons,custom_addons -u restaurant_product
```

If the module has not been installed before, update the Apps List and install it from the Apps menu instead of using `-u`.

### Usage

After installation:

1. Open the Products menu.
2. Create or open a product.
3. Enter the weight, calories, and expiration date in the added fields.
4. Use the **Large Meals** menu to view products matching the module's weight filter.

### Notes

- The weight field is an integer field; the module does not define a unit of measurement.
- The calories field is a floating-point field.
- The expiration date field is a date field.
- The large-meal filter uses a weight threshold greater than `200`.

---

## العربية

### نظرة عامة

**Restaurant Product** هو موديول مخصص لنظام Odoo، يعمل على توسيع الموديل القياسي `product.template` لإضافة بيانات إضافية تساعد في إدارة منتجات المطاعم والوجبات.

### المميزات

- إضافة حقل **وزن المنتج**.
- إضافة حقل **السعرات الحرارية للمنتج**.
- إضافة حقل **تاريخ انتهاء المنتج**.
- إظهار الحقول الإضافية في واجهة نموذج المنتج (Form View).
- إظهار وزن المنتج وتاريخ انتهائه في عرض Kanban.
- إضافة فلتر للبحث عن المنتجات التي يزيد وزنها عن `200`.
- إضافة قائمة **الوجبات الكبيرة** لعرض المنتجات مع تطبيق فلتر الوزن تلقائياً.

### التفاصيل التقنية

| العنصر | التفاصيل |
|---|---|
| اسم الموديول التقني | `restaurant_product` |
| اسم الموديول | Restaurant Product |
| الإصدار | `1.0.0` |
| الموديل الذي تم توسيعه | `product.template` |
| الاعتماديات | `product`, `sale` |
| الملفات الأساسية | `models.py`, `views.xml`, `__manifest__.py` |

### التثبيت

1. انسخ مجلد `restaurant_product` إلى مجلد الإضافات المخصصة (Custom Addons) في Odoo.
2. تأكد من إضافة مسار مجلد Custom Addons إلى إعداد `--addons-path`.
3. أعد تشغيل خادم Odoo.
4. فعّل وضع المطور (Developer Mode) عند الحاجة، ثم افتح قائمة **Apps**.
5. اختر **Update Apps List** لتحديث قائمة التطبيقات.
6. ابحث عن **Restaurant Product** ثم اضغط **Install**.

مثال على أمر التشغيل والتحديث، مع تعديل اسم قاعدة البيانات والمسارات حسب بيئتك:

```bash
python odoo-bin -d YOUR_DATABASE --addons-path=addons,custom_addons -u restaurant_product
```

إذا لم يكن الموديول مثبتاً من قبل، حدّث قائمة التطبيقات ثم ثبّته من قائمة Apps بدلاً من استخدام `-u`.

### طريقة الاستخدام

بعد تثبيت الموديول:

1. انتقل إلى قائمة المنتجات (Products).
2. أنشئ منتجاً جديداً أو افتح منتجاً موجوداً.
3. أدخل وزن المنتج والسعرات الحرارية وتاريخ الانتهاء في الحقول المضافة.
4. استخدم قائمة **الوجبات الكبيرة** لعرض المنتجات التي تطابق فلتر الوزن الموجود في الموديول.

### ملاحظات

- حقل الوزن من النوع Integer، ولا يحدد الموديول وحدة قياس للوزن.
- حقل السعرات الحرارية من النوع Float.
- حقل تاريخ الانتهاء من النوع Date.
- يعتمد فلتر الوجبات الكبيرة على شرط أن يكون الوزن أكبر من `200`.

---

## Author

**Abumajid**
