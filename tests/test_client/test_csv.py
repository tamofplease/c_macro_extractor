import os
from src.client.csv import CsvClient

DB_PATH = '.'
TABLE_NAME = 'example'
TGT_PATH = DB_PATH + '/' + TABLE_NAME + '.csv'
columns = ['id', 'name', 'url']
data1 = ('data1_id', 'data1_name', 'data1_url')
data2 = ('data2_id', 'data2_name', 'data2_url')
data3 = ('data3_id', 'data3_name', 'data3_url')

client = CsvClient(db_path=DB_PATH)


def test_to_create_csv_file():
    table_columns: tuple[str, ...] = client.create_table(
        table_name=TABLE_NAME, columns=columns)

    assert table_columns == columns
    assert os.path.exists(TGT_PATH)


def test_insert_to_csv_file():
    assert len(data1) == len(columns)

    inserted_data: tuple[str, ...] = client.insert(
        table_name=TABLE_NAME, data=data1)

    assert len(inserted_data) == len(data1)


def test_list_all():
    inserted_data = client.list_all(table_name=TABLE_NAME)

    assert len(data1) == len(inserted_data[0])
    assert data1[0] == inserted_data[0]['id']
    assert data1[1] == inserted_data[0]['name']
    assert data1[2] == inserted_data[0]['url']


def test_find_by():
    client.insert(
        table_name=TABLE_NAME, data=data2)
    client.insert(
        table_name=TABLE_NAME, data=data3)

    result: list[dict[str, str]] = client.find_by(
        table_name=TABLE_NAME, prop='id', value='data1_id')

    assert len(result) == 1
    assert len(result[0]) == len(columns)
    assert result[0]['id'] == data1[0]
    assert result[0]['name'] == data1[1]
    assert result[0]['url'] == data1[2]
