import django_tables2 as tables

class HotelTable(tables.Table):
    class Meta:
        model = Hotel

