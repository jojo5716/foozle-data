from slackclient import SlackClient

from ..apps.configuration.models import Configuration


def notify_error(error):
    config = Configuration.objects.first()
    
    if config and config.slack_token and config.slack_notify:
        sc = SlackClient(config.slack_token)

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
            channel=config.slack_channel,
            text=message,
            as_user='true:'
        )