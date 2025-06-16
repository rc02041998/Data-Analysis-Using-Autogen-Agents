import os
from dotenv import load_dotenv
from autogen import config_list_from_json

load_dotenv()

config_list = config_list_from_json("OAI_CONFIG_LIST")

llm_config = {
    "config_list": config_list,
    "temperature": 0,
    "cache_seed": 42,
}
print("Loaded config list:", config_list)