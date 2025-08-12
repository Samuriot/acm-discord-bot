import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
user = os.environ.get("SUPABASE_USER")
password = os.environ.get("SUPABASE_PW")

supabase = create_client(url, key)

authorize_req = supabase.auth.sign_in_with_password({
    "email": user,
    "password": password
})

access_tok = authorize_req.session.access_token
refresh_tok = authorize_req.session.refresh_token
supabase_client = create_client(url, key)
supabase_client.auth.set_session(access_tok, refresh_tok)