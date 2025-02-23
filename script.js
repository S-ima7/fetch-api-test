// GitHub APIからユーザー情報を取得する
async function fetchGitHubUserInfo(username) {
    const url = `https://api.github.com/users/${username}`;
    const response = await fetch(url);
  
    // OKステータス(200系)ならJSONを読み取り、必要なデータを返す
    if (response.ok) {
      const data = await response.json();
      const userLogin = data.login || "N/A";
      const userId    = data.id    || "N/A";
      const userBio   = data.bio   || "N/A";
  
      return `
  ● ユーザー名: ${userLogin}
  ● ユーザーID: ${userId}
  ● 自己紹介文: ${userBio}
  `;
    } else {
      // エラー時にはメッセージを投げる
      const errorMsg = `ユーザー情報を取得できませんでした。\n`
                     + `・ユーザー名が正しいか確認してください\n`
                     + `・レスポンスコード: ${response.status}`;
      throw new Error(errorMsg);
    }
  }
  
  // ボタンを押したときの処理を設定
  document.getElementById("fetchButton").addEventListener("click", async () => {
    const usernameInput = document.getElementById("usernameInput");
    const resultArea = document.getElementById("result");
    const errorArea = document.getElementById("error");
  
    // 表示をリセット
    resultArea.textContent = "";
    errorArea.textContent = "";
  
    // 入力されたユーザー名を取得
    const username = usernameInput.value.trim();
    if (!username) {
      errorArea.textContent = "ユーザー名を入力してください。";
      return;
    }
  
    try {
      // APIコール → 結果を表示
      const info = await fetchGitHubUserInfo(username);
      resultArea.textContent = info;
    } catch (err) {
      // エラー時の表示
      errorArea.textContent = err.message;
    }
  });
  