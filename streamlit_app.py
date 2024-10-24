# Streamlitライブラリをインポート
import streamlit as st
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('らっきーあにまる')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前は？')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'こんにちは、{user_input}さん！今日のあなたのラッキーアニマルを教えるよ') 
    else:
        st.error('名前を入力してね')  # エラーメッセージを表示

animals = ['うさぎ','ねこ','いぬ','なまけもの','ごりら','りす','こあら','ぱんだ']
results = random.choice(animals)
if st.button('えらぶ'):
    st.header(results)

