from slackclient import SlackClient


def notify_error(error_data):
    slack_token = "xoxb-212395692886-lpSzq7XxN0bFxhKrpsg5elFD"
    sc = SlackClient(slack_token)

    file_error = error_data.file_error
    message
    message = """ 
    Hola! @channel

    A un probre desgraciado le ha sucedido un error de js en mobilis.
    Podeis mirarlo?

    Gracias:
    ``` 
    El fichero donde se produjo el error es {}

    {}
    ```
    """.format(error_data.file_error, error_data.message)

    sc.api_call(
        "chat.postMessage",
        channel="G80NH489J",
        text=message,
        as_user='true:'
    )