from letesend import SMS

AUTH_TOKEN = "755d399dc182f11bec23425998e11256090b30b9"

SMS.login(auth_token=AUTH_TOKEN)

SMS.send(
    title='Company',
    to='+2250758660911',
    body='Hello World fron leteSend !'
)