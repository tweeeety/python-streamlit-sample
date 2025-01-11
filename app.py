import streamlit as st
import pandas as pd

st.title('streamlit Tutorial')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('Hello World!')

# st.write()はMarkdown表記対応
st.write('# headline1')
# 以下のように明示的に書くことも可能
st.markdown('# headline2')

st.write(['apple', 'orange', 'banana'])

# ダミーデータの作成
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
    })

# DataFrameを表示
st.write(df)

# st.dataframe()でも表示可能
st.dataframe(df)

# ボタンの表示
if st.button('Say hello'):
    st.write('Hello World!')

# チェックボックスの表示
if st.checkbox('Show/Hide'):
    st.write('Some text')

# ラジオボタンの表示
option = st.radio(
    'Which number do you like best?', 
    ['1', '2', '3']
)

# セレクトボックスの表示
option = st.selectbox(
    'Which number do you like best?', 
    ['1', '2', '3']
)

# マルチセレクトボックスの表示
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    default=['Yellow', 'Red'] # デフォルトの設定
)

# スライダーの表示
value = st.slider('Select a value', 0, 100, 50) # min, max, default

# テキスト入力の表示
# テキスト入力ボックス
text_input = st.text_input('Input', 'Input some text here.')
# テキストエリア
text_area = st.text_area('Text Area', 'Input some text here.')
input_num = st.number_input('Input a number', value=0)


# ぐるぐるまーくの表示
if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write('end!')


# サイドバーの表示
# Sidebarの選択肢を定義する
options = ["Option 1", "Option 2", "Option 3"]
choice = st.sidebar.selectbox("Select an option", options)

# Mainコンテンツの表示を変える
if choice == "Option 1":
    st.write("You selected Option 1")
elif choice == "Option 2":
    st.write("You selected Option 2")
else:
    st.write("You selected Option 3")


# カラムの分割
# ダミーデータの作成
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

# 2列のカラムを作成
col1, col2 = st.columns(2)

# col1にテキストを表示
with col1:
    st.header("Column 1")
    st.write("This is column 1.")

# col2にDataFrameを表示
with col2:
    st.header("Column 2")
    # DataFrameを表示
    st.write(df)


result = input_num ** 2
st.write('Result: ', result)
