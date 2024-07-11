import datetime
import time
import hashlib


class HashingCommands:
    def __init__(self, client, tree):
        self.client = client
        self.tree = tree
        self.register_HashingCommands()

    def register_HashingCommands(self):
        @self.tree.command(name="md5", description="Get the MD5 hash for a string")
        async def md5(interaction, string: str):
            await interaction.response.send_message(hashlib.md5(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha1", description="Get the SHA1 hash for a string")
        async def sha1(interaction, string: str):
            await interaction.response.send_message(hashlib.sha1(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha256", description="Get the SHA256 hash for a string")
        async def sha256(interaction, string: str):
            await interaction.response.send_message(hashlib.sha256(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha512", description="Get the SHA512 hash for a string")
        async def sha512(interaction, string: str):
            await interaction.response.send_message(hashlib.sha512(string.encode('utf-8')).hexdigest(), ephemeral=True)
