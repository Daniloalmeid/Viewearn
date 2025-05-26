from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from spl.token.instructions import transfer_checked, TransferCheckedParams
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.client import Token

# ⚠️ Coloque sua chave secreta como um array de 64 números inteiros
ISSUER_SECRET_KEY = [/* SUA CHAVE AQUI */]
issuer_keypair = Keypair.from_secret_key(bytes(ISSUER_SECRET_KEY))

TOKEN_MINT_ADDRESS = "SEU_TOKEN_MINT_ADDRESS_AQUI"
DECIMALS = 9

solana_client = Client("https://api.devnet.solana.com")

def enviar_token_para_usuario(destinatario_wallet: str, quantidade_tokens: float):
    token = Token(
        conn=solana_client,
        pubkey=PublicKey(TOKEN_MINT_ADDRESS),
        program_id=TOKEN_PROGRAM_ID,
        payer=issuer_keypair
    )

    issuer_token_account = token.get_or_create_associated_account_info(issuer_keypair.public_key)
    destinatario_token_account = token.get_or_create_associated_account_info(PublicKey(destinatario_wallet))

    transaction = Transaction()
    transaction.add(
        transfer_checked(
            TransferCheckedParams(
                program_id=TOKEN_PROGRAM_ID,
                source=issuer_token_account.address,
                mint=token.pubkey,
                dest=destinatario_token_account.address,
                owner=issuer_keypair.public_key,
                amount=int(quantidade_tokens * (10 ** DECIMALS)),
                decimals=DECIMALS
            )
        )
    )

    response = solana_client.send_transaction(transaction, issuer_keypair)
    return response
