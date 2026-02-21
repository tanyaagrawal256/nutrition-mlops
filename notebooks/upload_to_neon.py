import pandas as pd
from sqlalchemy import create_engine

# 🔴 Paste your Neon direct connection string here
connection_string = "postgresql://neondb_owner:npg_u9o0mjYZrKGL@ep-super-term-a1vhyv6l.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(connection_string)

# Load dataset
df = pd.read_csv("/Users/tanyaagrawal/nutrition_mlops/data/Personalized_Diet_Recommendations.csv")

# Upload to Neon
df.to_sql("nutrition_data", engine, if_exists="replace", index=False)

print("✅ Dataset uploaded successfully!")