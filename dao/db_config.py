import sqlite3
import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_XYs3akEOHm8R@ep-solitary-salad-b8g0lf0p-pooler.c-14.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    return sqlite3.connect(DB_PATH)