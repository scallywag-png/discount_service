import json
import urllib.request


url = "http://127.0.0.1:8000/api/apply-promo/"


data = {
    "code": "TEST",
    "cart_total": 1000
}


json_data = json.dumps(data).encode('utf-8')
req = urllib.request.Request(
    url,
    data=json_data,
    headers={'Content-Type': 'application/json'}
)

print(f"Відправляю запит: код '{data['code']}' на суму {data['cart_total']}...")


try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())

        print("\nСервер відповів:")
        print(f"   Стара ціна: {result['original_price']} грн")
        print(f"   Знижка:     {result['discount_amount']} грн")
        print(f"   Нова ціна:  {result['new_price']} грн")
        print(f"   Повідомлення: {result['message']}")

except urllib.error.HTTPError as e:

    print(f"\n Помилка від сервера: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(f"\nЩось зламалося: {e}")