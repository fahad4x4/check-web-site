# check-web-site

> A simple Python script that checks whether a list of websites is up or down and prints the results as a colored table.

[English](#english) | [العربية](#arabic)

![Python](https://img.shields.io/badge/python-3-blue?logo=python&logoColor=white)

---

<a id="english"></a>

## English

### Overview

`check.py` sends an HTTP GET request to each website in its `websites` list and reports whether the site responded successfully. The results are printed as a table showing each website, its status (**UP** in green or **DOWN** in red), and the HTTP status code or the error message.

### Features

- Checks any number of websites defined in a single list.
- 10-second timeout per website, so one slow site does not block the run.
- Marks a site **DOWN** on connection errors, timeouts, or HTTP 4xx/5xx responses (redirects are followed).
- Shows the HTTP code for sites that are up and the error message for sites that are down.
- Colored output (via `colorama`) in a neat grid table (via `tabulate`).
- Sends an identifying `User-Agent` header with each request.

### Requirements

- Python 3
- Packages listed in `requirements.txt`: `requests`, `colorama`, `tabulate`

### Installation

```bash
git clone https://github.com/fahad4x4/check-web-site.git
cd check-web-site
pip install -r requirements.txt
```

### Usage

1. Open `check.py` and edit the `websites` list with the sites you want to check:

   ```python
   websites = [
       "https://www.google.com",
       "https://github.com",
       "https://www.wikipedia.org",
   ]
   ```

2. Run the script:

   ```bash
   python3 check.py
   ```

Example output (colors not shown):

```text
╒═══════════════════════════╤══════════╤═════════════╕
│ Website                   │ Status   │   HTTP Code │
╞═══════════════════════════╪══════════╪═════════════╡
│ https://www.google.com    │ UP       │         200 │
├───────────────────────────┼──────────┼─────────────┤
│ https://github.com        │ UP       │         200 │
├───────────────────────────┼──────────┼─────────────┤
│ https://www.wikipedia.org │ UP       │         200 │
╘═══════════════════════════╧══════════╧═════════════╛
```

To change the timeout, edit `TIMEOUT = 10` in `check.py`.

### Project structure

```text
check-web-site/
├── check.py           # the website checker
├── requirements.txt   # Python dependencies
└── README.md
```

### License

Released under the [MIT License](LICENSE). Copyright © 2026 Fahad ALGhathbar (فهد الغثبر).

### Author

**Fahad ALGhathbar** — GitHub: [@fahad4x4](https://github.com/fahad4x4)

---

<a id="arabic"></a>

<div dir="rtl">

## العربية

### نظرة عامة

يرسل السكربت `check.py` طلب HTTP من نوع GET إلى كل موقع في قائمة `websites`، ثم يبيّن هل استجاب الموقع بنجاح أم لا. وتُعرض النتائج في جدول يوضح اسم الموقع وحالته (**UP** باللون الأخضر أو **DOWN** باللون الأحمر) ورمز حالة HTTP أو رسالة الخطأ.

### المزايا

- فحص أي عدد من المواقع المحددة في قائمة واحدة.
- مهلة انتظار قدرها 10 ثوانٍ لكل موقع، حتى لا يُعطّل موقع بطيء بقية الفحص.
- اعتبار الموقع متوقفًا **DOWN** عند أخطاء الاتصال أو انتهاء المهلة أو استجابات HTTP من فئتي 4xx و5xx (مع تتبّع عمليات إعادة التوجيه).
- عرض رمز HTTP للمواقع العاملة، ورسالة الخطأ للمواقع المتوقفة.
- مخرجات ملونة (عبر `colorama`) في جدول منسق (عبر `tabulate`).
- إرسال ترويسة `User-Agent` تعريفية مع كل طلب.

### المتطلبات

- Python 3
- الحزم المذكورة في `requirements.txt`: ‏`requests` و`colorama` و`tabulate`

### التثبيت

```bash
git clone https://github.com/fahad4x4/check-web-site.git
cd check-web-site
pip install -r requirements.txt
```

### طريقة الاستخدام

1. افتح الملف `check.py` وعدّل قائمة `websites` بالمواقع التي تريد فحصها:

   ```python
   websites = [
       "https://www.google.com",
       "https://github.com",
       "https://www.wikipedia.org",
   ]
   ```

2. شغّل السكربت:

   ```bash
   python3 check.py
   ```

مثال على المخرجات (دون الألوان):

```text
╒═══════════════════════════╤══════════╤═════════════╕
│ Website                   │ Status   │   HTTP Code │
╞═══════════════════════════╪══════════╪═════════════╡
│ https://www.google.com    │ UP       │         200 │
├───────────────────────────┼──────────┼─────────────┤
│ https://github.com        │ UP       │         200 │
├───────────────────────────┼──────────┼─────────────┤
│ https://www.wikipedia.org │ UP       │         200 │
╘═══════════════════════════╧══════════╧═════════════╛
```

لتغيير مهلة الانتظار، عدّل القيمة `TIMEOUT = 10` في الملف `check.py`.

### هيكل المشروع

```text
check-web-site/
├── check.py           # سكربت فحص المواقع
├── requirements.txt   # متطلبات Python
└── README.md
```

### الرخصة

المشروع منشور برخصة [MIT](LICENSE). حقوق النشر © 2026 فهد الغثبر (Fahad ALGhathbar).

### المؤلف

**فهد الغثبر** — حساب GitHub: [@fahad4x4](https://github.com/fahad4x4)

</div>
