import aiohttp,asyncio
class HimazinAPI():
    def __init__(self,token):
        self.token = token
        self.auth = aiohttp.BasicAuth(login=self.token)

    async def gchats(self):
        async with aiohttp.ClientSession() as aioclient:
            async with aioclient.get("https://www.kizuki1749.net/cgi/discordbot/globalchat.php") as resp:
                resp.raise_for_status()
                if resp.status == 200:
                    resp.json()

if __name__ == "__main__":
    #Debug mode
    loop = asyncio.get_event_loop()
    c = HimazinAPI(token="test_token")
    loop.run_until_complete(c.gchats())
