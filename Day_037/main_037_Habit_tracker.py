import requests
import datetime as dt
import os

USERNAME = ''
TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ID = ''

today = dt.datetime.now()

headers = {
    'X-USER-TOKEN': TOKEN,
}

def new_graph():
    graph_params = {
        'id': GRAPH_ID,
        'name': '100_days_of_code',
        'unit': 'min',
        'type': 'int',
        'color': 'shibafu',
    }

    new_pixela_graph = requests.post(url=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs', json=graph_params, headers=headers)
    print(new_pixela_graph.text)


def post_pixel():
    pixel_params = {
        'date': today.strftime('%Y%m%d'),
        'quantity': '120',
    }

    new_pixel = requests.post(
        url=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}',
        json=pixel_params,
        headers=headers
    )
    print(new_pixel.text)


def update_pixel():
    update_params = {
        'quantity': '10',
    }
    update_pixela_pixel = requests.put(
        url=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}',
        json=update_params,
        headers=headers,
    )
    print(update_pixela_pixel.text)


def delete_pixel():
    delete_pixela_pixel = requests.delete(
        url=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}',
        headers=headers,
    )
    print(delete_pixela_pixel.text)


def main():
    post_pixel()
    # update_pixel()
    # delete_pixel()


if __name__ == "__main__":
    main()
