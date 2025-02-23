import tkinter as tk
import requests

def get_user_info(username_entry, result_label, error_label):
    """
    GitHub APIを叩いてユーザー情報を取得し、画面に表示する関数
    ※ボタンのコールバックで呼び出される
    """
    # 入力されたユーザ名を取得 --
    username = username_entry.get().strip()  # テキスト入力からユーザ名を取得
    
    url = f"https://api.github.com/users/{username}"

    # APIからデータを取ってきてそのままログに出す（デバッグ用） ---
    response = requests.get(url)
    print("=== [DEBUG] Raw Response ===")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(data)  # 取得したJSONをそのまま出力（デバッグ）

        # 取ってきたデータから必要なものだけを取り出してログにだす
        user_login = data.get("login", "N/A")
        user_id    = data.get("id", "N/A")
        user_bio   = data.get("bio", "N/A")

        print(f"UserName: {user_login}")
        print(f"ID      : {user_id}")
        print(f"Bio     : {user_bio}")

        # ログじゃなくて画面に出してみる ---
        # 見た目（改行や文言など）を整える ---
        result_label.config(text=(
            f"● ユーザー名: {user_login}\n"
            f"● ユーザーID: {user_id}\n"
            f"● 自己紹介文: {user_bio}"
        ))
        error_label.config(text="", fg="black")  #エラー表示を消す
    else:
        # エラーハンドリング（ユーザーが見つからない、通信エラーなど） ---
        result_label.config(text="")
        error_msg = (
            "ユーザー情報を取得できませんでした。\n"
            "・ユーザー名が正しいか確認してください\n"
            f"・レスポンスコード: {response.status_code}"
        )
        error_label.config(text=error_msg, fg="red")


def setup_gui():
    """
    tkinterでウィンドウやウィジェットを生成・配置する関数
    """
    # メインウィンドウ（トップレベルウィンドウ）を作成
    root = tk.Tk()
    root.title("GitHub User Info")

    # フレーム（ウィジェットをグループ化して配置や余白を管理するためのコンテナ） 
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    # ラベル: テキスト表示に使うウィジェット
    username_label = tk.Label(frame, text="GitHubユーザー名:")
    # grid: 行・列を指定してウィジェットを配置するレイアウトマネージャ
    username_label.grid(row=0, column=0, sticky="w")

    # エントリー: テキスト入力欄
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=5)

    # ボタンを押すと取得しに行く ---
    fetch_button = tk.Button(
        frame, 
        text="取得", 
        command=lambda: get_user_info(username_entry, result_label, error_label)
    )
    fetch_button.grid(row=0, column=2)

    # 結果表示用ラベル（ユーザー名、ID、自己紹介を表示）
    result_label = tk.Label(frame, text="", justify="left", fg="blue")
    result_label.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")

    # エラー表示用ラベル
    error_label = tk.Label(frame, text="", fg="red")
    error_label.grid(row=2, column=0, columnspan=3, sticky="w")

    return root


def main():
    """
    メイン関数: アプリケーションの起動フローをまとめる
    """
    # GUIをセットアップしてウィンドウを取得
    root = setup_gui()

    # イベントループの開始（ウィンドウが閉じられるまで処理を継続）
    root.mainloop()


if __name__ == "__main__":
    main()
