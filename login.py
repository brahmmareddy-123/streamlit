
import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LR"
    )

def register_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s OR email=%s",
        (username, email)
    )
    user = cursor.fetchone()

    if user:
        st.error("❌ Username or Email already exists")
    else:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        conn.commit()
        st.success("✅ Registration successful")

    cursor.close()
    conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user

st.title("🔐 User Authentication")

st.sidebar.title("📋 Menu")
menu = st.sidebar.radio(
    "Choose an option",
    ["🔑 Login", "📝 Register"]
)

if menu == "🔑 Login":
    st.subheader("🔑 Login")

    username = st.text_input("👤 Username", key="login_username")
    password = st.text_input("🔒 Password", type="password", key="login_password")

    if st.button("Login"):
        if login_user(username, password):
            st.success("✅ Login successful")
        else:
            st.error("❌ Invalid username or password")

else:
    st.subheader("📝 Register")

    username = st.text_input("👤 Username", key="reg_username")
    email = st.text_input("📧 Email", key="reg_email")
    password = st.text_input("🔒 Password", type="password", key="reg_password")
    confirm_password = st.text_input("🔐 Confirm Password", type="password", key="reg_confirm")

    if st.button("Register"):
        if not username or not email or not password or not confirm_password:
            st.warning("⚠️ Please fill all fields")
        elif password != confirm_password:
            st.error("❌ Passwords do not match")
        else:
            register_user(username, email, password)

import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LR"
    )

def register_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s OR email=%s",
        (username, email)
    )
    user = cursor.fetchone()

    if user:
        st.error("❌ Username or Email already exists")
    else:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        conn.commit()
        st.success("✅ Registration successful")

    cursor.close()
    conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user

st.title("🔐 User Authentication")

st.sidebar.title("📋 Menu")
menu = st.sidebar.radio(
    "Choose an option",
    ["🔑 Login", "📝 Register"]
)

if menu == "🔑 Login":
    st.subheader("🔑 Login")

    username = st.text_input("👤 Username", key="login_username")
    password = st.text_input("🔒 Password", type="password", key="login_password")

    if st.button("Login"):
        if login_user(username, password):
            st.success("✅ Login successful")
        else:
            st.error("❌ Invalid username or password")

else:
    st.subheader("📝 Register")

    username = st.text_input("👤 Username", key="reg_username")
    email = st.text_input("📧 Email", key="reg_email")
    password = st.text_input("🔒 Password", type="password", key="reg_password")
    confirm_password = st.text_input("🔐 Confirm Password", type="password", key="reg_confirm")

    if st.button("Register"):
        if not username or not email or not password or not confirm_password:
            st.warning("⚠️ Please fill all fields")
        elif password != confirm_password:
            st.error("❌ Passwords do not match")
        else:
            register_user(username, email, password)

