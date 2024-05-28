// 画像のURLの配列（仮のデータ）
const imageUrls = ["https://newsatcl-pctr.c.yimg.jp/dk/expert-image/wankosoba/article/01654671/title-1706859691037.jpeg?exp=10800"];

// ランダムなインデックスを取得
const randomIndex = Math.floor(Math.random() * imageUrls.length);

// 画像を表示する要素を取得
const imageElement = document.getElementById("randomImage");

// ランダムな画像のURLを設定
imageElement.src = imageUrls[randomIndex];