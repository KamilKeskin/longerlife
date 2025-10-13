import streamlit as st, pandas as pd
from snowflake.snowpark import Session

st.set_page_config(page_title="LongLive · Snowflake", layout="wide")

@st.cache_resource
def sf_session():
    cfg = st.secrets["snowflake"]
    return Session.builder.configs({
        "account":   cfg["account"],
        "user":      cfg["user"],
        "password":  cfg["password"],
        "role":      cfg["role"],
        "warehouse": cfg["warehouse"],
        "database":  cfg["database"],
        "schema":    cfg["schema"],
    }).create()

# Connect
try:
    session = sf_session()
    #st.success("Connected to Snowflake ✅")
except Exception as e:
    st.error("Snowflake connection failed.")
    st.exception(e)
    st.stop()

# Context
ctx = session.sql("""
select current_user() user,
       current_role() role,
       current_account() account,
       current_region() region,
       current_warehouse() wh,
       current_database() db,
       current_schema() sch
""").to_pandas()
st.subheader("Context")
st.dataframe(ctx, use_container_width=True)

# Demo data
st.subheader("LONGLIVE.CORE.SHOWCASE_SALES")
try:
    df = session.sql("select * from LONGLIVE.CORE.SHOWCASE_SALES order by id").to_pandas()
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.warning("SHOWCASE_SALES not found or no access.")
    st.exception(e)

# Read-only query
st.subheader("Run SELECT")
q = st.text_area("SQL (SELECT only):",
                 "select count(*) as row_count  from LONGLIVE.CORE.SHOWCASE_SALES",
                 height=90)
if st.button("Run"):
    if not q.strip().lower().startswith("select"):
        st.error("Only SELECT statements are allowed.")
    else:
        try:
            st.dataframe(session.sql(q).to_pandas(), use_container_width=True)
        except Exception as e:
            st.exception(e)
