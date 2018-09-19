from slackclient import SlackClient


def notify_error(error):
    slack_token = "xoxb-212395692886-PuBVNOnambhOlBcjiOkuwx4t"
    sc = SlackClient(slack_token)

    message = """ 
    Hola! @channel

    A un probre desgraciado le ha sucedido un error de js en mobilis.
    Podeis mirarlo?

    Gracias:
    ``` 
    El fichero donde se produjo el error es {}

    {}
    ```
    """.format(error.file_error, error.message)

    sc.api_call(
        "chat.postMessage",
        channel="G80NH489J",
        text=message,
        as_user='true:'
    )